from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(project_root))

from automation import AutomationAgent


def test_fallback_plan_creates_tasks():
    agent = AutomationAgent()
    plan = agent.plan("Create a weekly status report")

    assert isinstance(plan, list)
    assert len(plan) >= 1
    assert "task" in plan[0]
    assert "detail" in plan[0]


def test_onboarding_intent_outputs_onboarding_tasks():
    agent = AutomationAgent()
    plan = agent.plan("Automate onboarding")

    assert any("onboarding" in item["task"].lower() or "welcome" in item["task"].lower() for item in plan)
