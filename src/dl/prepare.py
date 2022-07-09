import os
import shutil
from typing import List

import cv2
from tqdm import tqdm
from src.dl import config as conf


def prepare_data(data_directory: str, output_directory: str) -> None:
    """
    Collects and assembles data from the given directory
    :param data_directory: path to the data directory
    :param output_directory: path to the output directory
    :return:
    """
    os.makedirs(output_directory, exist_ok=True)

    directories = get_all_directories(data_directory)
    for directory in tqdm(directories, desc="Preprocessing directories", position=0):

        os.makedirs(
            os.path.join(output_directory, os.path.basename(directory)), exist_ok=True
        )

        files = get_all_files(directory)
        for file in tqdm(files, leave=False, desc="Preprocessing files", position=1):
            file = lowercase_file_extension(file)
            get_data_type(file, output_directory)

    if conf.DATA_DIRECTORIES_TO_CONCATENATE:
        os.makedirs(os.path.join(output_directory,
                                 conf.NAME_CONCATENATED_DIRECTORY),
                    exist_ok=True)

        concatenate_multiple_directories_to_one(conf.DATA_DIRECTORIES_TO_CONCATENATE,
                                                output_directory,
                                                conf.NAME_CONCATENATED_DIRECTORY)
        for directory in conf.DATA_DIRECTORIES_TO_CONCATENATE:
            shutil.rmtree(os.path.join(output_directory, directory))


def lowercase_file_extension(file: str) -> str:
    """
    Returns the lowercase extension of the file
    """
    if os.path.basename(file)[-4:].isupper():
        return file[:-4] + file[-4:].lower()
    return file


def get_all_directories(directory: str) -> list:
    """
    Returns a list of all directories in the given directory
    :param directory: path to the directory
    :return: list of directories
    """
    return [
        os.path.join(directory, name)
        for name in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, name))
    ]


def get_all_files(directory: str) -> list:
    """
    Returns a list of all files in the given directory
    :param directory: path to the directory
    :return: list of files
    """
    return [os.path.join(directory, name) for name in os.listdir(directory)]


def get_data_type(file: str, output_directory: str) -> None:
    """
    Returns the data type of the file
    :param file: path to the file
    :param output_directory: path to the output directory
    :return:
    """
    if file.endswith(tuple(conf.VIDEO_FORMATS_SUPPORTED)):
        convert_video_to_frames(file, output_directory)
    else:
        copy_image_file_to_processed_dir(file, output_directory)


def copy_image_file_to_processed_dir(file_path: str, output_directory: str) -> None:
    """
    Moves the file to the output directory
    :param file_path: path to the file
    :param output_directory: path to the output directory
    :return:
    """
    parent_dir = os.path.basename(os.path.dirname(file_path))
    file_name = os.path.basename(file_path)
    new_file_path = os.path.join(output_directory, parent_dir, file_name)
    shutil.copyfile(file_path, new_file_path)


def concatenate_multiple_directories_to_one(directories_to_concatenate: List[str],
                                            output_directory: str,
                                            new_folder_name: str) -> None:
    """
    Concatenates all the files in the given directory to one folder.
    :param directories_to_concatenate: list of directories to concatenate
    :param output_directory: path to the output directory
    :param new_folder_name: name of the new folder
    :return:
    """
    if not directories_to_concatenate:
        return

    for directory in directories_to_concatenate:
        for file in os.listdir(os.path.join(output_directory, directory)):
            shutil.move(
                os.path.join(output_directory, directory, file),
                os.path.join(output_directory, new_folder_name),
            )


def convert_video_to_frames(video_path: str, output_path: str) -> None:
    """
    Converts a video to frames
    :param video_path: path to the video
    :param output_path: path to the output folder
    :return:
    """
    video = cv2.VideoCapture(video_path)
    count = 0

    while video.isOpened():
        success, image = video.read()
        if success:
            if count % conf.VIDEO_FRAME_RATE == 0:
                parent_dir = os.path.basename(os.path.dirname(video_path))
                file_name_without_extension = os.path.basename(video_path)[:-4]
                cv2.imwrite(
                    os.path.join(
                        output_path,
                        parent_dir,
                        f"{file_name_without_extension}_frame_{count}.jpg",
                    ),
                    image,
                )
            count += 1
        else:
            break

    video.release()


if __name__ == "__main__":
    prepare_data(conf.RAW_DATA_DIR, conf.PROCESSED_DATA_DIR)
