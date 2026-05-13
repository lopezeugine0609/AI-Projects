# GHL / n8n Lead Automation Suite

A meta automation project that demonstrates lead capture and routing integrations for:

- `fieldroutes`
- `callgear`
- `callrail`
- `meta project` orchestration for lead acquisition workflows

This project simulates how GoHighLevel, n8n, and lead tracking tools can work together to automate lead ingestion, enrichment, and campaign routing.

## Project Goals

- Model common lead automation flows for field service and call tracking
- Provide reusable connectors for FieldRoutes, CallGear, and CallRail
- Support a top-level meta orchestration flow for end-to-end lead delivery
- Include documentation, tests, and deployment-ready examples

## Setup

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Run the lead automation CLI

```bash
python -m ghl_n8n_leads.src.app --flow fieldroutes
```

Supported flows:

- `fieldroutes`
- `callgear`
- `callrail`
- `meta`

## Tests

```bash
pytest
```

## Project layout

- `src/` — integration simulation modules and CLI
- `tests/` — validation of automation flows
- `docs/` — architecture, usage, and extension notes
