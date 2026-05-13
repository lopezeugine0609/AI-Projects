# Workspace Overview

This workspace holds multiple AI projects in a shared repository layout.

## Projects

- `va_client_intake_agent/`
  - VA client intake assistant for US small businesses.
  - Includes lead scoring, pain point detection, package recommendation, CRM payloads, response drafts, docs, CLI, and tests.
- `va_inbox_triage_copilot/`
  - Inbox triage copilot for classifying emails, assigning SLA priority, extracting tasks, and drafting replies.
  - Includes daily digest logic, docs, CLI, and tests.
- `va_meeting_action_tracker/`
  - Meeting action tracker that converts transcripts into decisions, owners, due dates, task payloads, and follow-up emails.
  - Includes docs, CLI, and tests.
- `ai-sentiment-classifier/`
  - Sentiment analysis using a classic machine learning pipeline.
  - Includes model training, prediction, and documentation.
- `ai-automation/`
  - AI automation toolkit that generates task plans and simulates workflow execution.
  - Includes a CLI, optional OpenAI integration, and documentation.
- `ghl_n8n_leads/`
  - Lead automation suite for GoHighLevel and n8n workflows with FieldRoutes, CallGear, CallRail, and meta routing.
  - Includes project docs, CLI simulations, and tests.
- `n8n_templates/`
  - Reusable n8n workflow templates, including social posting, scheduling, speech transcription, and advanced lead orchestration.
  - Includes JSON template exports and documentation for importing into n8n.
- `ai_welding_defects/`
  - Welding defect image classification using a CNN and synthetic image generation.
  - Includes training, inference, a Jupyter notebook, and comprehensive docs.

## Repository Guidelines

- Keep each project self-contained with its own `README.md`, `requirements.txt`, and `docs/` folder.
- Use separate virtual environments for each project.
- Document architecture, usage, and contribution steps within each project.
- For US VA portfolio work, describe business outcomes first: speed, follow-up reliability, lead conversion, and fewer missed tasks.

## How to Use

- Navigate into a project directory before installing dependencies.
- Read the project `README.md` first to understand the purpose and setup.
- Use `pytest` within the chosen project to run unit tests.
