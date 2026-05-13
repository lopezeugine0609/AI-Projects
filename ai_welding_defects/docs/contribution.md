# Contribution Guidelines

This document describes how to extend and improve the `ai_welding_defects` project.

## Extending the dataset

- Replace the synthetic image generator in `src/data.py` with a real welding dataset.
- Add new defect categories, such as `undercut`, `slag_inclusion`, or `misalignment`.
- Improve synthetic realism by simulating weld bead texture and varying lighting.

## Model improvements

- Experiment with deeper CNN architectures or pretrained backbones.
- Add data augmentation for translation, rotation, and intensity variation.
- Introduce regularization such as batch normalization and dropout.

## Testing and validation

- Add dataset shape and label tests to `tests/`.
- Include integration tests for training and inference pipelines.
- Validate predictions across a holdout test set and record performance metrics.

## Notebook exploration

Use `notebooks/welding_defects_analysis.ipynb` to inspect how synthetic samples are generated and how the CNN architecture behaves.
