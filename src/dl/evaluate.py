import os

import numpy as np
from PIL import Image
from keras.models import load_model
from src.dl import config as conf

if __name__ == "__main__":
    model = load_model(
        os.path.join(
            conf.MODELS_CHECKPOINT_PATH, "resnet_ep_15_val_acc_0.9710366129875183.h5"
        )
    )

    image = Image.open(
        os.path.join(
            conf.PROCESSED_DATA_DIR,
            "cut-out printouts",
            "0001e96803--624d117b945cc50d051697b9_frame_0.jpg",
        )
    )

    resized_image = image.resize(conf.IMAGE_SHAPE)
    image_as_array = np.array(resized_image)

    array_with_batch_dimension = image_as_array[np.newaxis, :, :, :]

    predictions = model.predict(array_with_batch_dimension)
    print(predictions)
    # model.evaluate(os.path.join(conf.PROCESSED_DATA_DIR, "test", "images", "1.jpg"))
