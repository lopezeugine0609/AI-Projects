import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from intake_agent import LeadIntakeAutomation


def test_hot_lead_gets_operations_package():
    agent = LeadIntakeAutomation()

    brief = agent.analyze(
        {
            "name": "Sarah",
            "company": "Bright Path Dental",
            "message": "Urgent help needed this week for missed calls, appointment follow-up, email, and CRM cleanup.",
            "weekly_hours": 20,
            "monthly_budget": 1500,
        }
    )

    assert brief.priority == "hot"
    assert brief.recommended_package == "Operations Support"
    assert "lead response" in brief.pain_points
    assert "crm cleanup" in brief.pain_points
    assert brief.crm_payload["lead_score"] >= 80


def test_general_inquiry_still_creates_response():
    agent = LeadIntakeAutomation()

    brief = agent.analyze({"name": "Marcus", "company": "Local HVAC", "message": "Need admin help."})

    assert brief.priority in {"nurture", "warm"}
    assert brief.response_draft.startswith("Hi Marcus")
    assert brief.discovery_questions
