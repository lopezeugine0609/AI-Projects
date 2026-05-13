# Meeting Action Tracker

An automation project for a common operations problem: meetings create decisions and tasks, but follow-through often depends on someone manually rewriting notes afterward.

## Real-Life Problem

Teams lose momentum when meeting notes never become owned tasks. This project shows how an engineer can convert rough notes into decisions, owners, due dates, open questions, and follow-up emails.

## Features

- Extracts action items from transcript-style notes
- Detects owners and due dates from common meeting language
- Captures decisions and open questions
- Generates a follow-up email
- Produces a compact task board payload for ClickUp, Asana, Trello, or Notion

## Run Demo

```powershell
python src/app.py --transcript "Decision: launch the new intake form. Maria will update the CRM by Friday. Can you send the project recap tomorrow?"
```

## Test

```powershell
python -m pytest
```

## Portfolio Pitch

"The problem was weak meeting follow-through. I built a tracker that converts meeting notes into owner-based tasks, due dates, decisions, and follow-up emails."
