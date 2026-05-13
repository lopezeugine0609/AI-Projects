import os

from src.data import load_data
from src.model import create_pipeline, save_model, load_model


def test_data_loading():
    x_train, x_test, y_train, y_test = load_data()
    assert len(x_train) > 0
    assert len(x_test) > 0
    assert len(y_train) == len(x_train)
    assert len(y_test) == len(x_test)


def test_pipeline_fit_and_predict(tmp_path):
    x_train, x_test, y_train, y_test = load_data()
    pipeline = create_pipeline()
    pipeline.fit(x_train, y_train)
    predictions = pipeline.predict(x_test)
    assert len(predictions) == len(x_test)
    assert set(predictions).issubset({"positive", "negative"})


def test_model_save_and_load(tmp_path):
    x_train, _, y_train, _ = load_data()
    pipeline = create_pipeline()
    pipeline.fit(x_train, y_train)
    model_file = tmp_path / "sentiment_model.joblib"
    saved_path = save_model(pipeline)
    loaded_pipeline = load_model()
    assert loaded_pipeline.predict(["This was a nice movie."])[0] in {"positive", "negative"}
    if os.path.exists(saved_path):
        os.remove(saved_path)
