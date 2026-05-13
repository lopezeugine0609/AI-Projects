# Welding Defect Classification Architecture

This project uses a convolutional neural network to classify synthetic weld images into defect categories.

## Core Components

- `src/data.py`
  - Generates synthetic weld images and defect labels.
  - Produces train/validation/test splits.
- `src/model.py`
  - Builds a 3-layer CNN with pooling and dropout.
  - Trains using sparse categorical crossentropy.
  - Saves and loads the Keras model.
- `src/train.py`
  - Orchestrates dataset creation, model building, training, evaluation, and model export.
- `src/predict.py`
  - Loads a saved model and runs inference on synthetic samples.

## Deep Learning Details

- Input images are grayscale and normalized to `[0, 1]`.
- The CNN uses convolutional blocks to learn spatial features of weld defects.
- Early stopping helps avoid overfitting on the synthetic training data.
- Classification is performed with a final softmax activation over defect categories.
