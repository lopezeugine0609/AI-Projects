# AI Projects Workspace

This repository contains multiple AI-focused Python projects organized as separate subdirectories.

## Included Projects

- `lead_intake_automation/`
  - A lead intake automation project that scores inquiries, detects pain points, recommends next steps, and drafts a first response.
- `inbox_triage_automation/`
  - An inbox operations project that classifies emails, assigns SLA priority, extracts tasks, and drafts response-ready replies.
- `meeting_action_tracker/`
  - A meeting follow-up assistant that turns transcripts into decisions, owner-based action items, due dates, and recap emails.
- `ai-sentiment-classifier/`
  - A movie review sentiment classification project with training, prediction, and documentation.
- `ai-automation/`
  - A new AI automation toolkit project with task planning, simulated execution, and CLI usage.
- `ghl_n8n_leads/`
  - A GHL/n8n lead automation suite modeling FieldRoutes, CallGear, CallRail, and meta lead routing.
- `ai_welding_defects/`
  - A welding defect image classification project with CNN training, synthetic data, and defect detection docs.

## Repository Structure

- `README.md` — workspace overview and pointers to each project.
- `docs/` — workspace-level documentation for project architecture and new automation features.
- `docs/operations-automation-roadmap.md` — project positioning for real-world operations automation case studies.
- `lead_intake_automation/` — inquiry intake, lead scoring, and CRM brief project.
- `inbox_triage_automation/` — inbox triage, SLA, task extraction, and reply draft project.
- `meeting_action_tracker/` — meeting summary, action tracking, and follow-up project.
- `ai-sentiment-classifier/` — existing AI sentiment classifier project.
- `ai-automation/` — new AI automation project.
- `ghl_n8n_leads/` — new GHL/n8n lead automation project.
- `n8n_templates/` — reusable n8n workflow templates for Facebook posting, scheduling, transcription, and multi-channel lead automation.
- `ai_welding_defects/` — new welding defect classification project.
- `.env` — environment variables and secret values (ignored by Git).
- `.gitignore` — repository ignore rules.

## Getting Started

1. Choose a project directory.
2. Create and activate a Python virtual environment.
3. Install the project dependencies with `pip install -r requirements.txt`.
4. Follow the project-specific README and `docs/` files.

## Portfolio Landing Page

A deployable portfolio page is available at `index.html` in the repository root. It is ready for GitHub Pages or any static site host.

To deploy on GitHub Pages:

1. Push this repository to GitHub.
2. Enable GitHub Pages in the repository settings using the `main` or `master` branch.
3. Select the root directory as the source.

## New Automation Project

The new `ai-automation/` project is designed to demonstrate a reusable AI automation pattern with:

- task intent planning
- action sequence generation
- optional LLM integration via `OPENAI_API_KEY`
- CLI execution
- automated tests

See `ai-automation/README.md` and `docs/ai-automation.md` for full details.

