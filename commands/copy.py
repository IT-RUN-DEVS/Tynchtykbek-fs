import os.path
import shutil

def copy(src, dest):
    if not os.path.exists(src):
        print('Файла с таким именем не существует!')

    if not os.path.exists(dest):
        os.makedirs(dest)

    shutil.copy(src, os.path.join(os.getcwd(), dest))
    print('Файл успешно скопирован!')
