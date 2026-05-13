from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class IntakeBrief:
    lead_name: str
    company: str
    priority: str
    score: int
    recommended_package: str
    pain_points: List[str]
    next_steps: List[str]
    discovery_questions: List[str]
    response_draft: str
    crm_payload: Dict[str, object]


class LeadIntakeAutomation:
    """Creates an operations-ready brief from a new inquiry."""

    PAIN_POINT_KEYWORDS = {
        "scheduling": ["appointment", "calendar", "schedule", "booking", "reschedule"],
        "inbox management": ["email", "inbox", "reply", "follow-up", "follow up"],
        "lead response": ["lead", "missed call", "call", "quote", "estimate"],
        "crm cleanup": ["crm", "pipeline", "ghl", "hubspot", "contacts"],
        "billing support": ["invoice", "billing", "payment", "receipt"],
        "customer support": ["customer", "support", "ticket", "complaint", "review"],
        "social admin": ["facebook", "instagram", "post", "content", "social"],
    }

    PACKAGE_RULES = [
        ("Operations Support", 75, "Best for daily admin ownership, CRM updates, follow-ups, and communication."),
        ("Growth Support", 50, "Best for lead response, social admin, inbox triage, and pipeline support."),
        ("Starter Support", 0, "Best for focused weekly admin help and simple repeatable workflows."),
    ]

    def analyze(self, inquiry: Dict[str, object]) -> IntakeBrief:
        name = str(inquiry.get("name") or "New lead").strip()
        company = str(inquiry.get("company") or "Unknown company").strip()
        message = str(inquiry.get("message") or "").strip()
        text = " ".join(str(value) for value in inquiry.values()).lower()

        pain_points = self._detect_pain_points(text)
        score = self._score(inquiry, text, pain_points)
        priority = self._priority(score)
        package = self._recommend_package(score)
        next_steps = self._build_next_steps(priority, pain_points)
        discovery_questions = self._build_questions(pain_points)
        response_draft = self._draft_response(name, company, package, pain_points)

        crm_payload = {
            "contact_name": name,
            "company": company,
            "lead_score": score,
            "priority": priority,
            "recommended_package": package,
            "pain_points": pain_points,
            "source": inquiry.get("source", "portfolio-demo"),
            "summary": self._summary(message, pain_points),
        }

        return IntakeBrief(
            lead_name=name,
            company=company,
            priority=priority,
            score=score,
            recommended_package=package,
            pain_points=pain_points,
            next_steps=next_steps,
            discovery_questions=discovery_questions,
            response_draft=response_draft,
            crm_payload=crm_payload,
        )

    def _detect_pain_points(self, text: str) -> List[str]:
        matches = [
            label
            for label, keywords in self.PAIN_POINT_KEYWORDS.items()
            if any(keyword in text for keyword in keywords)
        ]
        return matches or ["general admin support"]

    def _score(self, inquiry: Dict[str, object], text: str, pain_points: List[str]) -> int:
        score = 20 + min(len(pain_points) * 10, 40)

        if any(word in text for word in ["urgent", "today", "this week", "asap", "missed"]):
            score += 20
        if any(word in text for word in ["dental", "real estate", "law", "medical", "home service"]):
            score += 10
        if int(inquiry.get("weekly_hours") or 0) >= 15:
            score += 15
        if int(inquiry.get("monthly_budget") or 0) >= 1000:
            score += 15

        return min(score, 100)

    def _priority(self, score: int) -> str:
        if score >= 80:
            return "hot"
        if score >= 55:
            return "warm"
        return "nurture"

    def _recommend_package(self, score: int) -> str:
        for package, threshold, _description in self.PACKAGE_RULES:
            if score >= threshold:
                return package
        return "Starter Support"

    def _build_next_steps(self, priority: str, pain_points: List[str]) -> List[str]:
        steps = [
            "Send a same-day response with a clear discovery call option.",
            "Create CRM record with detected pain points and package recommendation.",
        ]
        if priority == "hot":
            steps.insert(0, "Offer two call slots within the next business day.")
        if "lead response" in pain_points:
            steps.append("Ask for current lead sources and missed-call handling process.")
        if "crm cleanup" in pain_points:
            steps.append("Request a sample pipeline export or screen recording.")
        return steps

    def _build_questions(self, pain_points: List[str]) -> List[str]:
        questions = [
            "What tasks consume the most owner or manager time each week?",
            "Which time zone should be covered for urgent replies?",
        ]
        if "scheduling" in pain_points:
            questions.append("What calendar and booking tools are currently used?")
        if "inbox management" in pain_points:
            questions.append("How many inboxes should be monitored daily?")
        if "lead response" in pain_points:
            questions.append("What is the ideal response time for new leads?")
        return questions

    def _draft_response(self, name: str, company: str, package: str, pain_points: List[str]) -> str:
        pain_text = ", ".join(pain_points)
        return (
            f"Hi {name}, thanks for reaching out about support for {company}. "
            f"Based on your note, the biggest opportunities look like {pain_text}. "
            f"I would recommend starting with the {package} package so we can stabilize the workflow, "
            "document repeatable steps, and improve response time. Would you like me to send two discovery call options?"
        )

    def _summary(self, message: str, pain_points: List[str]) -> str:
        if message:
            return f"{message[:180]} | Detected needs: {', '.join(pain_points)}"
        return f"Detected needs: {', '.join(pain_points)}"
