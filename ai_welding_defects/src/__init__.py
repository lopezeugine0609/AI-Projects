"""AI welding defect detection package."""
from .data import CLASS_NAMES, generate_synthetic_weld_images, get_dataset
from .model import build_cnn_model, load_model, save_model, train_model
