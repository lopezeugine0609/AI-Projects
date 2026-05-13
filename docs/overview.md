# Workspace Overview

This workspace holds multiple AI projects in a shared repository layout.

## Projects

- `ai-sentiment-classifier/`
  - Sentiment analysis using a classic machine learning pipeline.
  - Includes model training, prediction, and documentation.
- `ai-automation/`
  - AI automation toolkit that generates task plans and simulates workflow execution.
  - Includes a CLI, optional OpenAI integration, and documentation.
- `ghl_n8n_leads/`
  - Lead automation suite for GoHighLevel and n8n workflows with FieldRoutes, CallGear, CallRail, and meta routing.
  - Includes project docs, CLI simulations, and tests.
- `ai_welding_defects/`
  - Welding defect image classification using a CNN and synthetic image generation.
  - Includes training, inference, a Jupyter notebook, and comprehensive docs.

## Repository Guidelines

- Keep each project self-contained with its own `README.md`, `requirements.txt`, and `docs/` folder.
- Use separate virtual environments for each project.
- Document architecture, usage, and contribution steps within each project.

## How to Use

- Navigate into a project directory before installing dependencies.
- Read the project `README.md` first to understand the purpose and setup.
- Use `pytest` within the chosen project to run unit tests.
