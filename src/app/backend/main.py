import os
import uuid
import cv2
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import numpy as np
from PIL import Image
from starlette.responses import JSONResponse

import inference
import config as conf


app = FastAPI()


@app.get("/")
def index():
    return {"message": "Welcome to the Anti Spoofing API"}


@app.post("/predict")
def predict(file: UploadFile = File(...)) -> JSONResponse:
    image = Image.open(file.file)
    resized_image = image.resize(conf.IMAGE_SHAPE)
    image_as_array = np.asarray(resized_image)
    prediction_object, image_as_array = inference.predict(image_as_array)
    name = f"{str(uuid.uuid4())}_{round(prediction_object.top_score, 3)}.jpg"
    cv2.imwrite(os.path.join("storage", name), np.asarray(image))
    return JSONResponse(
        content={
            "prediction": prediction_object.to_json(),
            "name": os.path.join(os.path.abspath("storage"), name),
        }
    )
