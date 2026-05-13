# AI Automation Architecture

The `ai-automation` project is built around a lightweight automation agent.

## Components

- `src/automation.py`
  - Contains `AutomationAgent`.
  - Supports rule-based task planning and optional OpenAI LLM planning.
- `src/app.py`
  - Command-line interface to submit automation tasks and print plans.
- `tests/`
  - Verifies the fallback planning flow and expected task structure.

## Data Flow

1. The user provides an automation intent via CLI.
2. `AutomationAgent.plan()` decides whether to use an LLM or fallback planner.
3. If OpenAI is configured, the agent sends a prompt to the API and parses a JSON response.
4. If LLM integration is not available, the fallback planner returns a deterministic task sequence.
5. The CLI prints the task plan to the console.
