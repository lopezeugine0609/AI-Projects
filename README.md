# AI Projects Workspace

This repository contains multiple AI-focused Python projects organized as separate subdirectories.

## Included Projects

- `va_client_intake_agent/`
  - A VA-focused client intake assistant that scores US business leads, detects pain points, recommends a service package, and drafts a first response.
- `va_inbox_triage_copilot/`
  - An inbox operations copilot that classifies emails, assigns SLA priority, extracts tasks, and drafts client-safe replies.
- `va_meeting_action_tracker/`
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
- `docs/us-va-client-project-roadmap.md` — recommended VA project positioning for US clients.
- `va_client_intake_agent/` — client intake, lead scoring, and CRM brief project.
- `va_inbox_triage_copilot/` — inbox triage, SLA, task extraction, and reply draft project.
- `va_meeting_action_tracker/` — meeting summary, action tracking, and follow-up project.
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

## Recommended VA Portfolio Path

For attracting US clients as a virtual assistant, lead with these projects:

1. `va_client_intake_agent/` — best first impression because it shows faster lead response and professional onboarding.
2. `va_inbox_triage_copilot/` — best for busy owners who need email, lead, billing, and support messages organized.
3. `va_meeting_action_tracker/` — best for showing operations discipline after discovery calls and weekly client meetings.

See `docs/us-va-client-project-roadmap.md` for client niches, positioning, and upgrade ideas.
