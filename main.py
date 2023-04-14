import os
import shutil
import tarfile


#создание нового файла
def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write('')
        print(f'File {file_name} created successfully!')
    except Exception as e:
        print(f'Error creating file {file_name}: {e}')


#список директорий и файлов
def list_files_and_directories(path):
    contents = os.listdir(path)
    files_and_directories = [name for name in contents if os.path.isdir(os.path.join(path, name)) or os.path.isfile(os.path.join(path, name))]

    print(files_and_directories)


#копирование файлов
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


#перемещение файла
def move_file(src_path, dest_path):
    shutil.move(src_path, dest_path)




#создание новой директории
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory {path} created.")
    else:
        print(f"Directory {path} already exists.")



