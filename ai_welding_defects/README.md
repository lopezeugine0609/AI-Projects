# AI Welding Defect Classification

A deep learning project for detecting weld defects using image classification.

## Project Summary

This project demonstrates a convolutional neural network (CNN) trained on synthetic weld imagery to classify defects such as:

- `no_defect`
- `crack`
- `porosity`

The code includes dataset generation, model training, inference, and documentation.

## Setup

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Train the model

```bash
python -m ai_welding_defects.src.train --epochs 15 --batch-size 32
```

## Run inference

```bash
python -m ai_welding_defects.src.predict --model-path models/welding_cnn.keras
```

## Project Layout

- `src/` — dataset generation, CNN model, training, and prediction scripts.
- `tests/` — unit tests.
- `docs/` — architecture and usage documentation.
- `notebooks/` — exploratory notebook showing dataset creation and model structure.
