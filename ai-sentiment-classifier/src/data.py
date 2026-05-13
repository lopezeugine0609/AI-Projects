from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split


def build_dataset() -> pd.DataFrame:
    records = [
        ("I loved this movie, it was fantastic and heartfelt.", "positive"),
        ("An amazing experience with great acting.", "positive"),
        ("The plot was exciting and kept me engaged.", "positive"),
        ("Terrible story, the pacing was awful.", "negative"),
        ("I hated the ending and the characters were boring.", "negative"),
        ("A disappointing film with poor dialogue.", "negative"),
        ("It was a fun watch with charming performances.", "positive"),
        ("The movie was forgettable and badly directed.", "negative"),
        ("A beautiful story told with warmth and humor.", "positive"),
        ("The acting saved an otherwise weak script.", "negative"),
    ]
    df = pd.DataFrame(records, columns=["text", "label"])
    return df


def load_data(test_size: float = 0.25, random_state: int = 42) -> Tuple[pd.Series, pd.Series, pd.Series, pd.Series]:
    dataframe = build_dataset()
    x = dataframe["text"]
    y = dataframe["label"]
    return train_test_split(x, y, test_size=test_size, random_state=random_state)
