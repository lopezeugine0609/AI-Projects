# VA Client Intake Agent

An AI-style intake system for virtual assistants serving US small businesses. It turns a raw inquiry into a CRM-ready brief, lead score, recommended VA package, discovery questions, and a polished first response.

## Why This Engages US Clients

US business owners usually care about response speed, organization, and whether a VA can understand their operation quickly. This project shows that you can qualify leads, summarize pain points, and respond professionally without waiting for a manager to review every message.

## Features

- Lead priority scoring based on urgency, budget, business type, and admin workload
- Pain point detection for scheduling, inbox, CRM, follow-up, billing, and customer support
- Package recommendation for starter, growth, or operations support
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

## Portfolio Pitch

"I built an intake assistant that helps a US business respond to new leads faster, qualify the client, recommend the right VA service package, and send a CRM-ready summary."
