# Architecture

This project implements a small sentiment analysis pipeline using classical machine learning.

## Components

- `src/data.py`
  - Generates a synthetic movie review dataset.
  - Splits data into training and testing sets.

- `src/model.py`
  - Builds a text classification pipeline using `TfidfVectorizer` and `LogisticRegression`.
  - Trains the model and saves it as a `joblib` artifact.
  - Evaluates predictions using accuracy and classification report metrics.

- `src/predict.py`
  - Loads the trained model from disk.
  - Exposes a prediction helper for new review text.

- `src/app.py`
  - Provides a CLI entry point for training and prediction.
  - Offers a simple user experience for command-line execution.

## Data Flow

1. The dataset is created in memory from example text samples.
2. Text data is converted to numeric features with TF-IDF vectorization.
3. The logistic regression classifier learns to separate positive and negative reviews.
4. The trained model is saved to `models/sentiment_model.joblib`.
5. New text input is loaded, vectorized, and predicted by the saved pipeline.
