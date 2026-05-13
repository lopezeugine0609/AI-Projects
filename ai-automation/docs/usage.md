# AI Automation Usage

## Setup

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Run sample automation

```bash
python -m ai_automation.src.app --task "automate onboarding for a new employee"
```

## Enable OpenAI integration

(Optional) Set `OPENAI_API_KEY` in your environment before running the app:

```bash
set OPENAI_API_KEY=your_openai_api_key
```

The project will still work without the key using a built-in fallback planner.

## Run tests

```bash
pytest
```
