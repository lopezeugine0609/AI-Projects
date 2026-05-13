# Inbox Triage Automation

An automation project for a common operations problem: inboxes collect sales, support, billing, scheduling, and vendor messages faster than a team can organize them.

## Real-Life Problem

Important messages get buried when every email looks equally urgent. This project shows how an engineer can classify messages, protect response times, extract work, and turn email into an action queue.

## Features

- Email category detection: lead, billing, scheduling, support, vendor, or internal admin
- Priority and SLA recommendation
- Task extraction from common request language
- Reply draft with professional operations tone
- Daily digest summary for stakeholder reporting

## Run Demo

```powershell
python src/app.py --sender "jane@example.com" --subject "Need quote today" --body "Can someone call me back today about pricing and availability?"
```

## Test

```powershell
python -m pytest
```

## Engineering Pitch

"The problem was inbox overload. I built a triage automation that turns incoming emails into categories, priorities, action items, response windows, and draft replies."
