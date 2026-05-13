import os
from typing import Dict, List, Optional

try:
    import openai
except ImportError:
    openai = None


class AutomationAgent:
    """A simple automation agent that plans tasks from intent text."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if self.api_key and openai:
            openai.api_key = self.api_key

    def plan(self, intent: str) -> List[Dict[str, str]]:
        """Generate a task plan from a user intent."""
        if self.api_key and openai:
            return self._llm_plan(intent)

        return self._fallback_plan(intent)

    def _fallback_plan(self, intent: str) -> List[Dict[str, str]]:
        intent_lower = intent.lower()
        tasks: List[Dict[str, str]] = []

        if "onboard" in intent_lower or "hire" in intent_lower:
            tasks = [
                {"task": "Create onboarding checklist", "detail": "Draft tasks, resources, and schedule."},
                {"task": "Share welcome package", "detail": "Send documents and access links."},
                {"task": "Schedule orientation", "detail": "Book meetings with key stakeholders."},
            ]
        elif "report" in intent_lower or "status" in intent_lower:
            tasks = [
                {"task": "Collect updates", "detail": "Gather progress from each team member."},
                {"task": "Draft report", "detail": "Summarize achievements and blockers."},
                {"task": "Review and send", "detail": "Share report with stakeholders."},
            ]
        else:
            tasks = [
                {"task": "Define the goal", "detail": "Clarify requirements and scope."},
                {"task": "Break down steps", "detail": "List the actions needed to complete the task."},
                {"task": "Execute the workflow", "detail": "Perform steps in order and confirm completion."},
            ]

        return tasks

    def _llm_plan(self, intent: str) -> List[Dict[str, str]]:
        prompt = (
            "Create a short task plan for the following automation request:\n\n"
            f"{intent}\n\n"
            "Return a JSON array of tasks with keys 'task' and 'detail'."
        )
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=250,
        )
        text = response.choices[0].message.content.strip()
        try:
            import json

            return json.loads(text)
        except Exception:
            return self._fallback_plan(intent)
