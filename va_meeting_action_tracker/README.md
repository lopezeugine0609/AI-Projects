# VA Meeting Action Tracker

A meeting operations assistant for virtual assistants. It converts rough call notes or transcripts into decisions, action items, owners, due dates, and a client-ready follow-up email.

## Why This Engages US Clients

US clients often lose momentum after calls because nobody turns discussion into clear execution. This project shows that you can run meeting follow-up like an operations partner.

## Features

- Extracts action items from transcript-style notes
- Detects owners and due dates from common meeting language
- Captures decisions and open questions
- Generates a follow-up email
- Produces a compact task board payload for ClickUp, Asana, Trello, or Notion

## Run Demo

```powershell
python src/app.py --transcript "Decision: launch the new intake form. Maria will update the CRM by Friday. Can you send the client recap tomorrow?"
```

## Test

```powershell
python -m pytest
```

## Portfolio Pitch

"I built a meeting tracker that converts client calls into owner-based tasks, due dates, decisions, and follow-up emails."
