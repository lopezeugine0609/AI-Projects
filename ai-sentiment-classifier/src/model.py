from pathlib import Path

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline

MODEL_DIR = Path(__file__).resolve().parent.parent / "models"
MODEL_PATH = MODEL_DIR / "sentiment_model.joblib"


def create_pipeline() -> Pipeline:
    return Pipeline([
        ("vectorizer", TfidfVectorizer(lowercase=True, stop_words="english", ngram_range=(1, 2))),
        ("classifier", LogisticRegression(max_iter=500, random_state=42)),
    ])


def train_model(x_train, y_train):
    pipeline = create_pipeline()
    pipeline.fit(x_train, y_train)
    return pipeline


def evaluate_model(model, x_test, y_test) -> dict:
    predictions = model.predict(x_test)
    report = classification_report(y_test, predictions, output_dict=True)
    accuracy = accuracy_score(y_test, predictions)
    return {
        "accuracy": float(accuracy),
        "report": report,
    }


def save_model(model):
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    return MODEL_PATH


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Train the model first.")
    return joblib.load(MODEL_PATH)
