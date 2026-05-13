# Architecture

The tracker keeps the demo simple and dependable:

1. Split transcript notes into sentences.
2. Detect decisions from explicit meeting markers.
3. Detect action items from owner/task language.
4. Detect due dates from common business phrases.
5. Generate a follow-up email and task board payload.

## Future Upgrade

Connect to Zoom, Google Meet transcripts, or Otter exports. Add an LLM to handle messy transcripts and sync the final tasks into ClickUp, Asana, Trello, or Notion.
