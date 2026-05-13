# VA Inbox Triage Copilot

An inbox operations assistant for virtual assistants who support US-based founders, clinics, agencies, and home service businesses. It classifies incoming emails, estimates SLA, extracts tasks, and drafts concise replies.

## Why This Engages US Clients

Many US clients hire a VA because their inbox is slow, messy, or leaking sales opportunities. This demo shows that you can protect response times, organize priorities, and turn messages into action.

## Features

- Email category detection: lead, billing, scheduling, support, vendor, or internal admin
- Priority and SLA recommendation
- Task extraction from common request language
- Reply draft with professional VA tone
- Daily digest summary for client reporting

## Run Demo

```powershell
python src/app.py --sender "jane@example.com" --subject "Need quote today" --body "Can someone call me back today about pricing and availability?"
```

## Test

```powershell
python -m pytest
```

## Portfolio Pitch

"I built an inbox triage assistant that turns client emails into priority queues, action items, response windows, and draft replies."
