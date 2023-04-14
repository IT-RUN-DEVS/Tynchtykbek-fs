import os

def list_files_and_directories(path):
    contents = os.listdir(path)
    files_and_directories = [name for name in contents if os.path.isdir(os.path.join(path, name)) or os.path.isfile(os.path.join(path, name))]

    print(files_and_directories)