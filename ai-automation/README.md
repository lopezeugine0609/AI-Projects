# AI Automation Toolkit

A new AI automation project for planning and simulating task workflows.

## Overview

This project shows how an automation agent can:

- parse a task intent
- generate a sequenced action plan
- simulate execution results
- support optional LLM-based planning via `OPENAI_API_KEY`

## Project Structure

- `src/` — source code for automation logic and CLI.
- `tests/` — automated unit tests.
- `docs/` — project-specific architecture and usage docs.
- `requirements.txt` — Python dependency list.

## Setup

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Run the CLI

```bash
python -m ai_automation.src.app --task "automate onboarding for a new hire"
```

## Run tests

```bash
pytest
```

## Notes

The project includes a fallback rule-based planning engine that works even without an OpenAI API key.
