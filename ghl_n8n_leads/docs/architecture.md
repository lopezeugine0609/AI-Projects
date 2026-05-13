# GHL / n8n Lead Automation Architecture

This project models a meta automation stack for lead generation, tracking, and routing using GoHighLevel and n8n-style integrations.

## Modules

- `src/fieldroutes.py`
  - Simulates FieldRoutes inbound lead capture and CRM enrichment.
- `src/callgear.py`
  - Simulates CallGear call tracking and campaign routing.
- `src/callrail.py`
  - Simulates CallRail call lead capture and nurture workflow triggering.
- `src/meta_project.py`
  - Orchestrates the full meta flow by combining all source integrations.
- `src/app.py`
  - CLI entrypoint to run individual or meta flows.

## Flow design

- Each integration flow returns a sequence of automation steps.
- The meta flow consolidates lead sources and pushes final records to GoHighLevel.
- The project is intentionally designed as a connector prototype; it can be extended with real API calls and n8n workflows.
