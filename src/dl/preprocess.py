from typing import Tuple
from tensorflow import keras
from src.dl import config as conf


def preprocess_the_data(data_directory: str) -> Tuple[str, str]:
    """
    Preprocesses the data in the given directory
    :param data_directory: path to the directory
    :return:
    """
    train_ds = keras.utils.image_dataset_from_directory(
        directory=data_directory,
        batch_size=conf.BATCH_SIZE,
        image_size=conf.IMAGE_SHAPE,
        validation_split=0.2,
        seed=conf.SEED,
        shuffle=True,
        subset="training",
    )

    validation_ds = keras.utils.image_dataset_from_directory(
        directory=data_directory,
        batch_size=conf.BATCH_SIZE,
        image_size=conf.IMAGE_SHAPE,
        seed=conf.SEED,
        validation_split=0.2,
        shuffle=True,
        subset="validation",
    )

    train_ds = train_ds.prefetch(buffer_size=conf.BATCH_SIZE)
    validation_ds = validation_ds.prefetch(buffer_size=conf.BATCH_SIZE)

    return train_ds, validation_ds
