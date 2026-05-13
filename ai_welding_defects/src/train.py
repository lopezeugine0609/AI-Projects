import argparse
from pathlib import Path

from .data import CLASS_NAMES, get_dataset
from .model import build_cnn_model, save_model, train_model
from sklearn.metrics import classification_report


def parse_args():
    parser = argparse.ArgumentParser(description="Train the welding defect detection model")
    parser.add_argument("--epochs", type=int, default=20, help="Number of training epochs")
    parser.add_argument("--batch-size", type=int, default=32, help="Batch size for training")
    parser.add_argument("--model-path", default="models/welding_cnn.keras", help="Saved Keras model path")
    parser.add_argument("--image-size", type=int, default=64, help="Square image size for synthetic inputs")
    return parser.parse_args()


def main():
    args = parse_args()
    (train_images, train_labels), (val_images, val_labels), (test_images, test_labels) = get_dataset(
        image_size=(args.image_size, args.image_size), num_samples=900
    )

    model = build_cnn_model(input_shape=(args.image_size, args.image_size, 1), num_classes=len(CLASS_NAMES))
    history = train_model(model, train_images, train_labels, val_images, val_labels, epochs=args.epochs, batch_size=args.batch_size)

    model_dir = Path(args.model_path)
    model_dir.parent.mkdir(parents=True, exist_ok=True)
    save_model(model, args.model_path)

    predictions = model.predict(test_images, verbose=0)
    predicted_labels = predictions.argmax(axis=-1)
    report = classification_report(test_labels, predicted_labels, target_names=CLASS_NAMES)

    print("\nTest classification report:\n")
    print(report)
    print(f"Model saved to: {args.model_path}")


if __name__ == "__main__":
    main()
