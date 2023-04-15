import os

#создание новой директории
def create_dir(path):
    if os.path.exists(path):
        print('Такая директория уже существует')
        return
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory {path} created.")
    else:
        print(f"Directory {path} already exists.")
