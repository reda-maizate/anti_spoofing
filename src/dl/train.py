import os
import tensorflow as tf
from keras.callbacks import ModelCheckpoint
from tqdm.keras import TqdmCallback
import wandb
from wandb.keras import WandbCallback
from src.dl.models.basemodel_resnet import model
from src.dl import config as conf
from src.dl.preprocess import preprocess_the_data


wandb.init(project="anti_spoofing", entity="reda-maizate", name="local-v1.1")


if __name__ == "__main__":
    # Create needed directories
    if not os.path.exists(conf.MODELS_CHECKPOINT_PATH):
        os.makedirs(conf.MODELS_CHECKPOINT_PATH, exist_ok=True)
    if not os.path.exists(conf.LOGS_DIR):
        os.makedirs(conf.LOGS_DIR, exist_ok=True)

    train_ds, val_ds = preprocess_the_data(conf.PROCESSED_DATA_DIR)

    callbacks = [
        ModelCheckpoint(
            filepath=os.path.join(
                conf.MODELS_CHECKPOINT_PATH,
                "resnet_ep_{epoch}_val_acc_{val_accuracy}.h5",
            ),
            monitor="val_loss",
            save_best_only=True,
            mode="auto",
            verbose=1,
        ),
        TqdmCallback(),
        WandbCallback(),
    ]

    wandb.config = {
        "epochs": conf.NUM_EPOCHS,
        "batch_size": conf.BATCH_SIZE,
        "early_stopping_patience": conf.EARLY_STOPPING_PATIENCE,
        "learning_rate": conf.LEARNING_RATE,
        "optimizer": conf.OPTIMIZER,
    }

    model.compile(
        optimizer=conf.OPTIMIZER(learning_rate=conf.LEARNING_RATE),
        loss=conf.LOSS,
        metrics=conf.METRICS,
    )

    with tf.device("/gpu:0"):
        model.fit(
            train_ds,
            epochs=conf.NUM_EPOCHS,
            callbacks=callbacks,
            validation_data=val_ds,
            verbose=0,
        )
