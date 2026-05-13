# Welding Defect Classification Documentation

This documentation page describes the new welding defect detection project in the repository.

## What it does

The `ai_welding_defects` project uses a convolutional neural network (CNN) to classify synthetic weld images into defect categories:

- `no_defect`
- `crack`
- `porosity`

It is intended as a deep learning example for defect detection in manufacturing scenes.

## Key components

- `ai_welding_defects/src/data.py`
  - Generates grayscale synthetic weld images with defect-like patterns.
  - Splits data into train/validation/test sets.
- `ai_welding_defects/src/model.py`
  - Defines the CNN architecture and training utilities.
- `ai_welding_defects/src/train.py`
  - Runs training and evaluation, then saves the trained model.
- `ai_welding_defects/src/predict.py`
  - Loads the saved model and runs inference on a synthetic test sample.
- `ai_welding_defects/notebooks/welding_defects_analysis.ipynb`
  - Demonstrates the dataset and model in a notebook-driven analysis.

## Usage

Follow the project README in `ai_welding_defects/README.md` and the project-specific docs in `ai_welding_defects/docs/`.
