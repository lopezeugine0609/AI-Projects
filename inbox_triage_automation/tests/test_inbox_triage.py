import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inbox_triage import InboxTriageCopilot


def test_new_lead_today_is_urgent():
    copilot = InboxTriageCopilot()

    result = copilot.triage(
        {
            "sender": "jane@example.com",
            "subject": "Need quote today",
            "body": "Can you call me back today about pricing and availability?",
        }
    )

    assert result.category == "new lead"
    assert result.priority == "urgent"
    assert "call-needed" in result.tags
    assert "Respond within 1 business hour" == result.sla


def test_daily_digest_counts_priorities():
    copilot = InboxTriageCopilot()
    results = [
        copilot.triage({"sender": "a@test.com", "subject": "Invoice", "body": "Please send receipt."}),
        copilot.triage({"sender": "b@test.com", "subject": "Schedule", "body": "Need to reschedule appointment."}),
    ]

    digest = copilot.daily_digest(results)

    assert digest["total_emails"] == 2
    assert digest["priority_counts"]["high"] == 1
    assert digest["priority_counts"]["normal"] == 1
