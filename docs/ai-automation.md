# AI Automation Project Documentation

This document describes the new `ai-automation` project and its architecture.

## Purpose

The automation project demonstrates how AI can help plan and simulate task execution for routine workflows. It is built as a lightweight Python toolkit with an extensible automation agent.

## Architecture

- `ai-automation/src/automation.py`
  - Defines the `AutomationAgent` that converts a user intent into a task plan.
  - Supports a fallback rule-based planner when an LLM is not configured.
- `ai-automation/src/app.py`
  - Provides a CLI to run sample automation requests.
- `ai-automation/tests/`
  - Contains unit tests for the automation planning logic.

## Usage

1. Create a virtual environment in `ai-automation`:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r ai-automation/requirements.txt
```

3. Run the automation CLI:

```bash
python -m ai_automation.src.app --task "create a weekly status report"
```

4. Run tests:

```bash
cd ai-automation
pytest
```

## Optional LLM Integration

If you want to enable LLM-powered planning, set `OPENAI_API_KEY` in your environment and install the optional `openai` dependency.

```bash
set OPENAI_API_KEY=your_key_here
```

The project will continue to work with a rule-based fallback when no key is available.
