# Lead Intake Automation

An automation project for a common operations problem: new inquiries arrive in messy text, but the team still needs a fast summary, lead score, recommended next step, discovery questions, and a polished first response.

## Real-Life Problem

Businesses lose opportunities when inquiries sit too long or get handled inconsistently. This project shows how an engineer can standardize the intake process and turn unstructured messages into structured action.

## Features

- Lead priority scoring based on urgency, budget, business type, and admin workload
- Pain point detection for scheduling, inbox, CRM, follow-up, billing, and customer support
- Service recommendation for starter, growth, or operations support
- CRM payload output for GoHighLevel, HubSpot, Airtable, or Google Sheets
- Discovery questions and first-response email draft

## Run Demo

```powershell
python src/app.py --name "Sarah" --company "Bright Path Dental" --message "We need help with appointment follow-up, inbox cleanup, and missed lead calls this week."
```

## Test

```powershell
python -m pytest
```

## Engineering Pitch

"The problem was inconsistent lead intake. I built an automation that scores inquiries, detects needs, recommends next steps, and produces a CRM-ready summary."
