import os
import uuid
import cv2
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import numpy as np
from PIL import Image
from starlette.responses import JSONResponse

from src.app.backend import inference
from src.app.backend import config as conf


app = FastAPI()


@app.get("/")
def index():
    return {"message": "Welcome to the Anti Spoofing API"}


@app.post("/predict")
def predict(file: UploadFile = File(...)) -> JSONResponse:
    # TODO: Trouver un moyen d'importer la librairie PyQT5.
    image = Image.open(file.file)
    # image.show()
    resized_image = image.resize(conf.IMAGE_SHAPE)
    image_as_array = np.asarray(resized_image)
    prediction_object, image_as_array = inference.predict(image_as_array)
    name = f"{str(uuid.uuid4())}_{round(prediction_object.top_score, 3)}.jpg"
    os.makedirs("storage", exist_ok=True)
    cv2.imwrite(os.path.join("storage", name), np.asarray(image))
    return JSONResponse(
        content={
            "prediction": prediction_object.to_json(),
            "name": os.path.join(os.path.abspath("storage"), name),
        }
    )


# if __name__ == "__main__":
# import uvicorn

# uvicorn.run(app, host="0.0.0.0", port=8080, debug=True)
