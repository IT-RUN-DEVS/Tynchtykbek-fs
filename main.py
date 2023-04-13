import os
import shutil
import tarfile


def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write('')
        print(f'File {file_name} created successfully!')
    except Exception as e:
        print(f'Error creating file {file_name}: {e}')


def list_files_and_directories(path):
    contents = os.listdir(path)
    files_and_directories = [name for name in contents if os.path.isdir(os.path.join(path, name)) or os.path.isfile(os.path.join(path, name))]

    print(files_and_directories)


def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'rb') as fsrc:
            with open(destination_file, 'wb') as fdst:
                # читаем содержимое исходного файла по блокам
                while True:
                    block = fsrc.read(1024)
                    if not block:
                        break
                    # записываем блок в целевой файл
                    fdst.write(block)
    except FileNotFoundError as e:
        print(f'Error: {e}')


def move_file(src_path, dest_path):
    """
    Move a file from src_path to dest_path.
    """
    shutil.move(src_path, dest_path)


def create_snapshot(snapshot_name, root_path):
    with tarfile.open(snapshot_name, "w:gz") as tar:
        tar.add(root_path, arcname=os.path.basename(root_path))


def backup(source_dir, dest_dir):
    shutil.copytree(source_dir, dest_dir)


