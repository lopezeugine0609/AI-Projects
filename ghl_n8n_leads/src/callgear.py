from typing import Dict, List


def callgear_lead_flow() -> List[Dict[str, str]]:
    """Simulate CallGear call tracking to lead generation flow."""
    return [
        {"step": "Capture CallGear call tracking event", "detail": "Extract inbound call metadata from CallGear webhook."},
        {"step": "Enrich lead data", "detail": "Append campaign and source information to the lead record."},
        {"step": "Route to GHL funnel", "detail": "Send the lead into the appropriate GoHighLevel funnel or pipeline."},
        {"step": "Log call event", "detail": "Store call details and recording links for sales review."},
        {"step": "Trigger automation", "detail": "Start n8n workflow for lead nurturing or verification."},
    ]
