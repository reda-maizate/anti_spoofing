import os

import requests
import streamlit as st
from PIL import Image

BACKEND_URL = os.environ["BACKEND_URL"]
BACKEND_API_PORT = os.environ["BACKEND_API_PORT"]

st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("Anti spoofing web app")

# displays a file uploader widget
image_uploaded = st.file_uploader("Choose an image")
image_camera = st.camera_input("Take a picture")


# displays a button
if st.button("Upload the image"):
    if image_uploaded is not None or image_camera is not None:
        image = image_uploaded or image_camera
        files = {"file": image.getvalue()}
        res = requests.post(f"{BACKEND_URL}:{BACKEND_API_PORT}/predict", files=files)
        img_path = res.json()
        image = Image.open(img_path.get("name"))
        st.image(image, width=500)
        st.text(f"Prediction label: {img_path.get('prediction').get('top_label')}")
        st.text(
            f"Prediction score: {round(img_path.get('prediction').get('top_score'), 3)}% of accuracy"
        )
        st.text(f"Scores: {img_path.get('prediction').get('scores')}")
