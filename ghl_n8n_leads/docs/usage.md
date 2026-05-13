# GHL / n8n Lead Automation Usage

## Setup

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Run a source flow

```bash
python -m ghl_n8n_leads.src.app --flow fieldroutes
```

Other supported flows:

- `callgear`
- `callrail`
- `meta`

## Example: run the meta orchestration

```bash
python -m ghl_n8n_leads.src.app --flow meta
```

## Run tests

```bash
pytest
```

## Notes

This project uses simulated connector logic to model how call-tracking and field service lead sources can be routed into a centralized GoHighLevel automation stack.
