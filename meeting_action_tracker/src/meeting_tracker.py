import re
from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class ActionItem:
    owner: str
    task: str
    due: str


@dataclass(frozen=True)
class MeetingSummary:
    decisions: List[str]
    action_items: List[ActionItem]
    open_questions: List[str]
    follow_up_email: str
    task_board_payload: List[Dict[str, str]]


class MeetingActionTracker:
    """Turns meeting notes into an operations-ready follow-up package."""

    ACTION_PATTERNS = [
        r"([A-Z][a-z]+) will ([^.?!]+)",
        r"([A-Z][a-z]+) to ([^.?!]+)",
        r"can you ([^.?!]+)",
        r"please ([^.?!]+)",
    ]

    DUE_KEYWORDS = [
        "today",
        "tomorrow",
        "friday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "next week",
        "end of week",
    ]

    def summarize(self, transcript: str, default_owner: str = "Automation Owner") -> MeetingSummary:
        sentences = self._sentences(transcript)
        decisions = self._decisions(sentences)
        open_questions = [
            sentence
            for sentence in sentences
            if sentence.endswith("?") and not sentence.lower().startswith(("can you", "please"))
        ]
        action_items = self._actions(sentences, default_owner)
        follow_up_email = self._follow_up(decisions, action_items, open_questions)
        payload = [
            {"owner": item.owner, "task": item.task, "due": item.due, "status": "to-do"}
            for item in action_items
        ]

        return MeetingSummary(
            decisions=decisions,
            action_items=action_items,
            open_questions=open_questions,
            follow_up_email=follow_up_email,
            task_board_payload=payload,
        )

    def _sentences(self, transcript: str) -> List[str]:
        raw_sentences = re.split(r"(?<=[.?!])\s+", transcript.strip())
        return [sentence.strip() for sentence in raw_sentences if sentence.strip()]

    def _decisions(self, sentences: List[str]) -> List[str]:
        decisions = []
        for sentence in sentences:
            lowered = sentence.lower()
            if lowered.startswith("decision:"):
                decisions.append(sentence.split(":", 1)[1].strip().rstrip("."))
            elif any(marker in lowered for marker in ["we decided", "approved", "confirmed"]):
                decisions.append(sentence.rstrip("."))
        return decisions or ["No explicit decisions captured"]

    def _actions(self, sentences: List[str], default_owner: str) -> List[ActionItem]:
        items: List[ActionItem] = []
        for sentence in sentences:
            for pattern in self.ACTION_PATTERNS:
                for match in re.findall(pattern, sentence, flags=re.IGNORECASE):
                    if isinstance(match, tuple):
                        owner, task = match
                    else:
                        owner, task = default_owner, match
                    items.append(ActionItem(owner=owner, task=self._clean_task(task), due=self._due(sentence)))

        if not items:
            items.append(ActionItem(owner=default_owner, task="Send meeting recap and confirm next steps", due="next business day"))
        return items

    def _clean_task(self, task: str) -> str:
        cleaned = task.strip().rstrip(".?!")
        for due in self.DUE_KEYWORDS:
            cleaned = re.sub(rf"\b(?:by )?{due}\b", "", cleaned, flags=re.IGNORECASE).strip()
        return cleaned[:1].upper() + cleaned[1:]

    def _due(self, sentence: str) -> str:
        lowered = sentence.lower()
        for due in self.DUE_KEYWORDS:
            if due in lowered:
                return due
        return "next business day"

    def _follow_up(self, decisions: List[str], actions: List[ActionItem], questions: List[str]) -> str:
        decision_lines = "\n".join(f"- {decision}" for decision in decisions)
        action_lines = "\n".join(f"- {item.owner}: {item.task} ({item.due})" for item in actions)
        question_lines = "\n".join(f"- {question}" for question in questions) if questions else "- None"
        return (
            "Hi team,\n\n"
            "Here is the meeting recap.\n\n"
            "Decisions:\n"
            f"{decision_lines}\n\n"
            "Action items:\n"
            f"{action_lines}\n\n"
            "Open questions:\n"
            f"{question_lines}\n\n"
            "I will track these items and follow up on anything due soon."
        )
