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


def delete(args):
    """
    Get the file name and delete
    """
    file_name = args.delete[0]
    validate_file(file_name)
    # Delete the file
    os.remove(file_name)
    print("File successfully deleted")


def copy(args):
    """
    Copy file
    """
    file_1 = args.copy[0]
    file_2 = args.copy[1]

    validate_file(file_1)
    # Validate the file 2
    if not validate_file_type(file_2):
        print(INVALID_FILE_TYPE_MESSAGE)
        exit()
    with open(file_1, 'r') as f1:
        with open(file_2, 'w') as f2:
            f2.write(f1.read())
    print("File successfully copy")


def rename(args):
    """
    Rename file
    """
    old_filename = args.rename[0]
    new_filename = args.rename[1]
    validate_file(old_filename)
    # validate the new file type
    if not validate_file_type(new_filename):
        print(INVALID_FILE_TYPE_MESSAGE)
        exit()
    os.rename(old_filename, new_filename)
    print("File is successfully rename")


def main():
    """
    Create parser object
    """
    parser = argparse.ArgumentParser(description="A text file manager CLI")
    # Read a file
    parser.add_argument('-r', '--read', type=str, nargs=1, metavar="file_name", default=None,
                        help="Open and read a specific file")
    # Delete a file
    parser.add_argument('-d', '--delete', type=str, nargs=1, metavar="file_name", default=None, help="Delete a file")
    # Copy a file
    parser.add_argument('-c', '--copy', type=str, nargs=2, metavar=('file_1', 'file_2'), help="Copy a file")
    # rename a file
    parser.add_argument('-rn', '--rename', type=str, nargs=2, metavar=('file_1', 'file_2'), help="Rename a file")

    # parse the argument from standard output
    args = parser.parse_args()
    if args.read is not None:
        read(args)
    if args.delete is not None:
        delete(args)
    if args.copy is not None:
        copy(args)
    if args.rename is not None:
        rename(args)


if __name__ == "__main__":
    main()
