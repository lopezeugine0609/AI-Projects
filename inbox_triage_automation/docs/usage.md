# Usage

Run a sample email through the triage assistant:

```powershell
python src/app.py --sender "jane@example.com" --subject "Need quote today" --body "Can you call me back today about pricing and availability?"
```

Use the result to show:

- how the automation protects response times
- which emails need urgent action
- what tasks should be added to ClickUp, Trello, Asana, or Google Sheets
- what draft reply can be sent after review
