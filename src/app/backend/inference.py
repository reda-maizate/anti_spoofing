from dataclasses import dataclass
from typing import List, Tuple

import numpy as np
from keras.saving.save import load_model

import config as conf


@dataclass
class PredictionModel:
    top_score: float
    top_label: str
    scores: dict

    @classmethod
    def from_predictions(cls, predictions: List[float]):
        return cls(
            top_score=round(float(np.max(predictions)), 3) * 100,
            top_label=conf.CLASSES[np.argmax(predictions)],
            scores={
                conf.CLASSES[index]: round(float(prediction), 3) * 100
                for index, prediction in enumerate(predictions)
            },
        )

    def to_json(self):
        return {
            "top_score": self.top_score,
            "top_label": self.top_label,
            "scores": self.scores,
        }

    def __str__(self):
        return f"Prediction(top_score={self.top_score}, top_label={self.top_label}, scores={self.scores})"


def predict(image_as_array: np.ndarray) -> Tuple[PredictionModel, np.ndarray]:
    model = load_model(conf.MODEL_PATH)
    array_with_batch_dimension = image_as_array[np.newaxis, :, :, :]

    predictions = model.predict(array_with_batch_dimension)
    prediction_object = PredictionModel.from_predictions(predictions=predictions[0])
    return prediction_object, image_as_array
