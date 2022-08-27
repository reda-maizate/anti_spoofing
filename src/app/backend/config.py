import os

# Model paths
MODEL_NAME = "resnet_ep_15_val_acc_0.9710366129875183.h5"
MODELS_PATH = os.path.join("..", "..", "dl", "models", "checkpoints")
MODEL_PATH = os.path.join(MODELS_PATH, MODEL_NAME)

# Preprocessing configurations
IMAGE_SHAPE = (256, 256)
CLASSES = {
    0: "cut-out printouts",
    1: "live",
    2: "live_selfie",
    3: "printouts",
    4: "replay",
}
