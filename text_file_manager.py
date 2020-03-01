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


def read(args):
    """
    get the file name and path and read
    """
    file_name = args.read[0]
    # validate the file
    validate_file(file_name)
    with open(file_name, 'r') as file:
        print(file.read())


def main():
    """
    Create parser object
    """
    parser = argparse.ArgumentParser(description="A text file manager CLI")
    parser.add_argument('-r', '--read', type=str, nargs=1, metavar="file_name", default=None,
                        help="Open and read a specific file")
    args = parser.parse_args()
    if args.read is not None:
        read(args)


if __name__ == "__main__":
    main()
