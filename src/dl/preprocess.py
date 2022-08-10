from typing import Tuple
import numpy as np
from tensorflow import keras
import matplotlib.image as mpimg
from src.dl import config as conf


def preprocess_the_data(data_directory: str) -> Tuple[str, str]:
    """
    Preprocesses the data in the given directory
    :param data_directory: path to the directory
    :return:
    """
    train_ds = keras.utils.image_dataset_from_directory(
        directory=data_directory,
        labels='inferred',
        label_mode='categorical',
        batch_size=conf.BATCH_SIZE,
        image_size=conf.IMAGE_SHAPE,
        seed=conf.SEED,
        shuffle=True,
        subset='training'
    )

    validation_ds = keras.utils.image_dataset_from_directory(
        directory=data_directory,
        labels='inferred',
        label_mode='categorical',
        batch_size=conf.BATCH_SIZE,
        image_size=conf.IMAGE_SHAPE,
        seed=conf.SEED,
        validation_split=0.2,
        shuffle=True,
        subset='validation'
    )
    return train_ds, validation_ds


def read_image(image_path: str) -> np.ndarray:
    """
    Reads the image from the given path
    :param image_path: path to the image
    :return: image
    """
    return mpimg.imread(image_path)


def reshape_image(image: np.ndarray, new_shape: Tuple[int, int]) -> np.ndarray:
    """
    Reshapes the image to the required shape
    :param new_shape: new shape of the image
    :param image: image to be reshaped
    :return: reshaped image
    """
    return image.reshape(new_shape)


def normalize_image(image: np.ndarray) -> np.ndarray:
    """
    Normalizes the image
    :param image: image to be normalized
    :return: normalized image
    """
    return image / 255


if __name__ == "__main__":
    preprocess_the_data(conf.PROCESSED_DATA_DIR)
