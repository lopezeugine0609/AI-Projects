from typing import Dict, List

from .fieldroutes import fieldroutes_lead_flow
from .callgear import callgear_lead_flow
from .callrail import callrail_lead_flow


def meta_lead_flow() -> List[Dict[str, str]]:
    """Create a meta orchestration flow for lead capture across multiple sources."""
    flow = [
        {"step": "Initialize lead routing engine", "detail": "Start the meta automation workflow."},
        {"step": "Ingest FieldRoutes source", "detail": "Process field service leads from FieldRoutes."},
        {"step": "Ingest CallGear source", "detail": "Process call tracking leads from CallGear."},
        {"step": "Ingest CallRail source", "detail": "Process call tracking leads from CallRail."},
        {"step": "Consolidate lead records", "detail": "Merge duplicates and enrich with campaign data."},
        {"step": "Dispatch to GHL", "detail": "Send final lead records into the GoHighLevel CRM and funnel."},
        {"step": "Trigger cross-channel nurture", "detail": "Launch email/SMS nurture workflows in n8n."},
    ]
    flow.extend(fieldroutes_lead_flow())
    flow.extend(callgear_lead_flow())
    flow.extend(callrail_lead_flow())
    return flow
