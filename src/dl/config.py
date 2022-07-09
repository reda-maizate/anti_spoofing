import os

# Data configurations and paths
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw_data")
PROCESSED_DATA_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "processed_data"
)
# (If needed)
DATA_DIRECTORIES_TO_CONCATENATE = ["live_video", "live_selfie"]
NAME_CONCATENATED_DIRECTORY = "live"

# Video configurations
VIDEO_FORMATS_SUPPORTED = [
    ".avi",
    ".mkv",
    ".mov",
    ".mp4",
    ".mpg",
    ".mpeg",
    ".wmv",
    ".3gp",
]
VIDEO_FRAME_RATE = 5

# Preprocessing configurations
IMAGE_SHAPE = (256, 256)
BATCH_SIZE = 32
SEED = 42
