# AI Sentiment Classifier

A simple Python AI project that trains and serves a movie-review sentiment classifier.
This repository includes training, inference, automated tests, and full documentation for Git push readiness.

## Project Overview

- `src/` contains the application code.
- `tests/` contains unit tests.
- `docs/` contains architecture, usage, and contribution documentation.
- `requirements.txt` lists Python dependencies.

## Features

- Synthetic sentiment dataset generation
- Text preprocessing with TF-IDF vectorization
- Logistic regression classifier
- CLI entrypoint for training and prediction
- Automated model evaluation metrics

## Setup

1. Create a virtual environment.

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Run training and evaluation.

```bash
python -m src.app --train
```

4. Run an example prediction.

```bash
python -m src.app --predict "That movie was fantastic and full of heart."
```

## Tests

```bash
pytest
```

## Git Push

```bash
git init
git add .
git commit -m "Initial AI sentiment classifier project"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

## Documentation

See `docs/architecture.md`, `docs/usage.md`, and `docs/contribution.md` for full project details.
