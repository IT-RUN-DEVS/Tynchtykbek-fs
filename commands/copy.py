import os.path
import shutil

def copy(source_file_path, destination_file_path):
    if not os.path.exists(source_file_path):
        print('Файла с таким именем не существует!')

    if not os.path.exists(destination_file_path):
        os.makedirs(destination_file_path)

    if os.path.isfile(source_file_path):
        shutil.copy(source_file_path, destination_file_path)
        print("Файл успешно скопирован!")

    if os.path.isdir(destination_file_path):
        shutil.copytree(source_file_path, destination_file_path)
        print('Папка успешно скопирована!')
