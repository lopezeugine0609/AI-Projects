import re
from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class TriageResult:
    sender: str
    category: str
    priority: str
    sla: str
    tasks: List[str]
    tags: List[str]
    reply_draft: str


class InboxTriageCopilot:
    """Classifies emails and turns them into action steps."""

    CATEGORY_KEYWORDS = {
        "new lead": ["quote", "pricing", "availability", "estimate", "consultation"],
        "scheduling": ["schedule", "reschedule", "calendar", "appointment", "meeting"],
        "billing": ["invoice", "payment", "receipt", "refund", "charge"],
        "customer support": ["issue", "problem", "complaint", "broken", "help"],
        "vendor": ["proposal", "contract", "supplier", "partnership", "vendor"],
        "internal admin": ["report", "update", "task", "document", "file"],
    }

    TASK_PATTERNS = [
        r"can you ([^.?!]+)",
        r"please ([^.?!]+)",
        r"need(?:s|ed)? to ([^.?!]+)",
        r"follow up(?: with)? ([^.?!]+)",
    ]

    def triage(self, email: Dict[str, str]) -> TriageResult:
        sender = email.get("sender", "unknown sender")
        subject = email.get("subject", "")
        body = email.get("body", "")
        text = f"{subject} {body}".lower()

        category = self._category(text)
        priority = self._priority(text, category)
        sla = self._sla(priority, category)
        tasks = self._extract_tasks(body, category)
        tags = self._tags(category, priority, text)
        reply_draft = self._draft_reply(sender, category, priority)

        return TriageResult(
            sender=sender,
            category=category,
            priority=priority,
            sla=sla,
            tasks=tasks,
            tags=tags,
            reply_draft=reply_draft,
        )

    def daily_digest(self, results: List[TriageResult]) -> Dict[str, object]:
        by_priority = {"urgent": 0, "high": 0, "normal": 0}
        categories: Dict[str, int] = {}

        for result in results:
            by_priority[result.priority] += 1
            categories[result.category] = categories.get(result.category, 0) + 1

        return {
            "total_emails": len(results),
            "priority_counts": by_priority,
            "category_counts": categories,
            "recommended_first_actions": [result.tasks[0] for result in results if result.tasks][:5],
        }

    def _category(self, text: str) -> str:
        scores = {
            category: sum(1 for keyword in keywords if keyword in text)
            for category, keywords in self.CATEGORY_KEYWORDS.items()
        }
        category, score = max(scores.items(), key=lambda item: item[1])
        return category if score else "internal admin"

    def _priority(self, text: str, category: str) -> str:
        if any(word in text for word in ["urgent", "asap", "today", "missed", "angry", "cancel"]):
            return "urgent"
        if category in {"new lead", "customer support", "billing"}:
            return "high"
        return "normal"

    def _sla(self, priority: str, category: str) -> str:
        if priority == "urgent":
            return "Respond within 1 business hour"
        if category == "new lead":
            return "Respond within 2 business hours"
        if priority == "high":
            return "Respond same business day"
        return "Respond within 1 business day"

    def _extract_tasks(self, body: str, category: str) -> List[str]:
        tasks: List[str] = []
        for pattern in self.TASK_PATTERNS:
            tasks.extend(match.strip().capitalize() for match in re.findall(pattern, body, flags=re.IGNORECASE))

        if not tasks:
            defaults = {
                "new lead": "Confirm interest, collect requirements, and offer next available call slot",
                "scheduling": "Check calendar availability and propose two time options",
                "billing": "Review invoice/payment status and respond with next step",
                "customer support": "Acknowledge the issue and create a support task",
                "vendor": "Review vendor message and summarize for stakeholder approval",
                "internal admin": "Review message and add any needed task to the admin tracker",
            }
            tasks.append(defaults[category])

        return tasks

    def _tags(self, category: str, priority: str, text: str) -> List[str]:
        tags = [category.replace(" ", "-"), priority]
        if "us" in text or "est" in text or "pst" in text or "cst" in text:
            tags.append("us-timezone")
        if "call" in text:
            tags.append("call-needed")
        return tags

    def _draft_reply(self, sender: str, category: str, priority: str) -> str:
        urgency_line = "I am prioritizing this now." if priority == "urgent" else "I will review this and follow up with the next step."
        return (
            f"Hi {sender.split('@')[0]}, thanks for the message. "
            f"I categorized this as {category}. {urgency_line} "
            "I will keep the thread organized and confirm once the action item is complete."
        )
