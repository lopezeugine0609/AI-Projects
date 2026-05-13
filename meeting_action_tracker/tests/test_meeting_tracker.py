import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from meeting_tracker import MeetingActionTracker


def test_extracts_decisions_actions_and_due_dates():
    tracker = MeetingActionTracker()

    summary = tracker.summarize(
        "Decision: launch the new intake form. Maria will update the CRM by Friday. "
        "Can you send the project recap tomorrow? What budget should we use?"
    )

    assert summary.decisions == ["launch the new intake form"]
    assert summary.action_items[0].owner == "Maria"
    assert summary.action_items[0].due == "friday"
    assert summary.action_items[1].owner == "Automation Owner"
    assert summary.action_items[1].due == "tomorrow"
    assert summary.open_questions == ["What budget should we use?"]


def test_defaults_when_no_action_items_exist():
    tracker = MeetingActionTracker()

    summary = tracker.summarize("We discussed the campaign status.")

    assert summary.action_items[0].task == "Send meeting recap and confirm next steps"
    assert summary.follow_up_email.startswith("Hi team")
