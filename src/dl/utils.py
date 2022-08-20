from typing import Tuple
import numpy as np
from matplotlib import image as mpimg


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
