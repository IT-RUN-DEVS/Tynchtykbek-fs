import os

def list_files_and_dirs(directory):

    files_and_dirs = os.listdir(directory)

    for item in files_and_dirs:
        if os.path.isdir(os.path.join(directory, item)):
            print(f'Dir: {item}')
        else:
            print(f'File: {item}')

print(os.getcwd())