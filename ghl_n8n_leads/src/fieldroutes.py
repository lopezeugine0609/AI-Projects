from typing import Dict, List


def fieldroutes_lead_flow() -> List[Dict[str, str]]:
    """Simulate ingestion of FieldRoutes leads into an automation pipeline."""
    return [
        {"step": "Receive FieldRoutes request", "detail": "Capture service request data from FieldRoutes webhook."},
        {"step": "Validate lead contact", "detail": "Normalize phone, email and address data for GoHighLevel."},
        {"step": "Create or update lead in CRM", "detail": "Push contact and opportunity details into GoHighLevel."},
        {"step": "Tag as FieldRoutes lead", "detail": "Use GHL tags to track source and route to campaign."},
        {"step": "Schedule follow-up", "detail": "Create calendar appointment or task for sales outreach."},
    ]
