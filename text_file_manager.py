import os
import argparse

INVALID_FILE_TYPE_MESSAGE = "Error: Invalid type of file, must be a .txt file"
INVALID_PATH_MESSAGE = "Error: Path does not exists"


def validate_file_type(file_name):
    """
    Validate file name
    """
    return file_name.endswith('.txt')


def validate_file_path(path):
    """
    Validate file path
    """
    return os.path.exists(path)


def validate_file(file_name):
    """
    Validate file name and file path
    """
    if not validate_file_path(file_name):
        print(INVALID_PATH_MESSAGE)
        quit()
    elif not validate_file_type(file_name):
        print(INVALID_FILE_TYPE_MESSAGE)
        quit()
    return













