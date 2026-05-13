# Usage

## Install dependencies

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Train the model

```bash
python -m src.app --train
```

This command builds the dataset, trains the classifier, evaluates it on a holdout set, and saves the model artifact to `models/sentiment_model.joblib`.

## Predict new text

```bash
python -m src.app --predict "I enjoyed the film and its characters."
```

## Run tests

```bash
pytest
```

## Project layout

- `README.md` — overview and Git push instructions.
- `src/` — source code for data, model, prediction, and CLI.
- `tests/` — unit tests for basic validation.
- `docs/` — documentation for architecture and usage.
