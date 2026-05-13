import tensorflow as tf


def build_cnn_model(input_shape=(64, 64, 1), num_classes=3):
    """Build a CNN for welding defect image classification."""
    model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Input(shape=input_shape),
            tf.keras.layers.Conv2D(32, 3, activation="relu", padding="same"),
            tf.keras.layers.MaxPooling2D(2),
            tf.keras.layers.Conv2D(64, 3, activation="relu", padding="same"),
            tf.keras.layers.MaxPooling2D(2),
            tf.keras.layers.Conv2D(128, 3, activation="relu", padding="same"),
            tf.keras.layers.MaxPooling2D(2),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dropout(0.35),
            tf.keras.layers.Dense(num_classes, activation="softmax"),
        ]
    )
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model


def train_model(model, train_images, train_labels, val_images, val_labels, epochs=20, batch_size=32):
    callbacks = [
        tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=4, restore_best_weights=True)
    ]
    history = model.fit(
        train_images,
        train_labels,
        validation_data=(val_images, val_labels),
        epochs=epochs,
        batch_size=batch_size,
        callbacks=callbacks,
        verbose=2,
    )
    return history


def save_model(model, path: str):
    if not path.endswith(".keras") and not path.endswith(".h5"):
        path = f"{path}.keras"
    model.save(path)
    return path


def load_model(path: str):
    if not path.endswith(".keras") and not path.endswith(".h5"):
        path = f"{path}.keras"
    return tf.keras.models.load_model(path)
