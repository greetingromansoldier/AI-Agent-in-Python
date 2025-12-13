import os

def get_files_info(working_directory="calculator", directory="."):
    working_dir_abs = os.path.abspath(working_directory)

    return working_dir_abs

if __name__ == "__main__":
    print(get_files_info())
