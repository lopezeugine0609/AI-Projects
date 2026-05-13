import argparse
import sys

from .data import load_data
from .model import evaluate_model, save_model, train_model
from .predict import predict_text


def train_and_save():
    x_train, x_test, y_train, y_test = load_data()
    model = train_model(x_train, y_train)
    evaluation = evaluate_model(model, x_test, y_test)
    path = save_model(model)
    print("Model trained and saved to:", path)
    print("Evaluation metrics:")
    print(f"Accuracy: {evaluation['accuracy']:.2f}")
    print("Classification report:")
    for label, metrics in evaluation["report"].items():
        if label in ["accuracy", "macro avg", "weighted avg"]:
            continue
        print(f"  {label}: precision={metrics['precision']:.2f}, recall={metrics['recall']:.2f}, f1-score={metrics['f1-score']:.2f}")


def run_prediction(text: str):
    try:
        sentiment = predict_text(text)
        print(f"Input: {text}")
        print(f"Predicted sentiment: {sentiment}")
    except FileNotFoundError as exc:
        print(exc)
        print("Run the script with --train first to create the model.")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="AI Sentiment Classifier")
    parser.add_argument("--train", action="store_true", help="Train the sentiment model")
    parser.add_argument("--predict", type=str, help="Predict sentiment for the provided text")
    args = parser.parse_args()

    if args.train:
        train_and_save()
    elif args.predict:
        run_prediction(args.predict)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
