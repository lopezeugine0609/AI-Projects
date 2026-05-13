from pathlib import Path

from .model import load_model


def predict_text(text: str) -> str:
    model = load_model()
    prediction = model.predict([text])
    return prediction[0]


def get_model_path() -> Path:
    return Path(__file__).resolve().parent.parent / "models" / "sentiment_model.joblib"
