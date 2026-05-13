import argparse
import numpy as np

from .data import CLASS_NAMES, generate_synthetic_weld_images
from .model import load_model


def parse_args():
    parser = argparse.ArgumentParser(description="Run inference on a welding defect image")
    parser.add_argument("--model-path", default="models/welding_cnn.keras", help="Path to the saved Keras model")
    parser.add_argument("--sample-index", type=int, default=None, help="Index of synthetic sample to predict")
    parser.add_argument("--image-size", type=int, default=64, help="Image size for synthetic sample generation")
    return parser.parse_args()


def main():
    args = parse_args()
    model = load_model(args.model_path)
    samples, labels = generate_synthetic_weld_images(num_samples=10, image_size=(args.image_size, args.image_size))

    index = args.sample_index
    if index is None:
        index = np.random.randint(0, len(samples))
    index = index % len(samples)

    sample = np.expand_dims(samples[index], axis=0)
    predicted = model.predict(sample, verbose=0)
    predicted_label = CLASS_NAMES[int(np.argmax(predicted))]
    actual_label = CLASS_NAMES[int(labels[index])]

    print(f"Sample index: {index}")
    print(f"Actual defect class: {actual_label}")
    print(f"Predicted defect class: {predicted_label}")


if __name__ == "__main__":
    main()
