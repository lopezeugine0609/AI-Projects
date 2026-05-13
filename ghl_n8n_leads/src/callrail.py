from typing import Dict, List


def callrail_lead_flow() -> List[Dict[str, str]]:
    """Simulate CallRail lead capture and distribution flow."""
    return [
        {"step": "Fetch CallRail call lead", "detail": "Retrieve caller information and lead source from CallRail."},
        {"step": "Map call to campaign", "detail": "Assign call leads to the matching GoHighLevel campaign."},
        {"step": "Create lead task", "detail": "Generate task for sales follow-up with lead details."},
        {"step": "Send SMS / email sequence", "detail": "Trigger follow-up automation in n8n based on tag rules."},
        {"step": "Store analytics", "detail": "Record conversion and call attribution data for reporting."},
    ]
