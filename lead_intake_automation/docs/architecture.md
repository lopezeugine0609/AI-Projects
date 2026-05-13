# Architecture

The project uses deterministic scoring so the demo is reliable without paid API access.

## Flow

1. Receive inquiry data from a form, email, or webhook.
2. Detect admin pain points from keywords.
3. Score the lead based on urgency, workload, budget, and business type.
4. Recommend a service package or next operational step.
5. Produce a CRM payload, response draft, next steps, and discovery questions.

## Future Upgrade

Add an LLM layer to rewrite the response draft in a brand voice, summarize long intake forms, and map leads to a CRM pipeline stage.
