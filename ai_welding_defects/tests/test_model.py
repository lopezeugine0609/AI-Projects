from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(project_root))

from data import generate_synthetic_weld_images
from model import build_cnn_model


def test_synthetic_dataset_shape():
    images, labels = generate_synthetic_weld_images(num_samples=30, image_size=(64, 64))
    assert images.shape == (30, 64, 64, 1)
    assert labels.shape == (30,)
    assert images.min() >= 0.0 and images.max() <= 1.0


def test_cnn_builds_successfully():
    model = build_cnn_model(input_shape=(64, 64, 1), num_classes=3)
    assert model.output_shape == (None, 3)


def test_model_can_train_on_small_batch():
    images, labels = generate_synthetic_weld_images(num_samples=60, image_size=(64, 64))
    model = build_cnn_model(input_shape=(64, 64, 1), num_classes=3)
    history = model.fit(images, labels, epochs=1, batch_size=16, verbose=0)
    assert history.history["loss"][-1] >= 0.0
