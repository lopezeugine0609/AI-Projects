import numpy as np
from typing import Tuple

CLASS_NAMES = ["no_defect", "crack", "porosity"]


def _draw_line(image: np.ndarray, start: Tuple[int, int], end: Tuple[int, int], width: int = 2):
    rr, cc = np.linspace(start[0], end[0], 100).astype(int), np.linspace(start[1], end[1], 100).astype(int)
    for dy, dx in zip(rr, cc):
        y0 = max(0, dy - width)
        y1 = min(image.shape[0], dy + width)
        x0 = max(0, dx - width)
        x1 = min(image.shape[1], dx + width)
        image[y0:y1, x0:x1] -= 0.6


def _draw_circle(image: np.ndarray, center: Tuple[int, int], radius: int = 4):
    y, x = np.ogrid[: image.shape[0], : image.shape[1]]
    mask = (x - center[1]) ** 2 + (y - center[0]) ** 2 <= radius ** 2
    image[mask] -= 0.5


def generate_synthetic_weld_images(num_samples: int = 600, image_size: Tuple[int, int] = (64, 64)):
    """Create synthetic grayscale weld images for defect classification."""
    height, width = image_size
    images = np.zeros((num_samples, height, width, 1), dtype=np.float32)
    labels = np.zeros((num_samples,), dtype=np.int32)

    for i in range(num_samples):
        base = np.random.normal(loc=0.5, scale=0.15, size=(height, width)).astype(np.float32)
        base = np.clip(base, 0.0, 1.0)

        class_id = i % len(CLASS_NAMES)
        labels[i] = class_id

        if class_id == 1:
            _draw_line(base, (height // 2, width // 8), (height // 2, width - width // 8), width=1)
            base += np.random.normal(0, 0.03, size=base.shape)
        elif class_id == 2:
            for center in [
                (height // 3, width // 3),
                (height // 2, width // 2),
                (height // 1.8, width // 1.5),
            ]:
                _draw_circle(base, center, radius=3)
            base += np.random.normal(0, 0.02, size=base.shape)

        images[i, :, :, 0] = np.clip(base, 0.0, 1.0)

    return images, labels


def get_dataset(split_ratio: float = 0.15, **kwargs):
    """Return train/validation/test splits for the welding defect dataset."""
    from sklearn.model_selection import train_test_split

    images, labels = generate_synthetic_weld_images(**kwargs)
    train_images, remainder_images, train_labels, remainder_labels = train_test_split(
        images, labels, test_size=2 * split_ratio, stratify=labels, random_state=42
    )
    val_images, test_images, val_labels, test_labels = train_test_split(
        remainder_images,
        remainder_labels,
        test_size=0.5,
        stratify=remainder_labels,
        random_state=42,
    )
    return (train_images, train_labels), (val_images, val_labels), (test_images, test_labels)
