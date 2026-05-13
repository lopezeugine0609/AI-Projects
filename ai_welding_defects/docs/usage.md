# Welding Defect Classification Usage

## Install dependencies

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Train the CNN

```bash
python -m ai_welding_defects.src.train --epochs 20 --batch-size 32
```

This command generates synthetic weld imagery, trains a CNN, evaluates the model, and saves it to `models/welding_cnn.keras`.

## Run prediction

```bash
python -m ai_welding_defects.src.predict --model-path models/welding_cnn.keras
```

The prediction script loads the saved model and evaluates a random synthetic sample.

## Notebook exploration

Open `notebooks/welding_defects_analysis.ipynb` to inspect model architecture, sample images, and training behavior.
