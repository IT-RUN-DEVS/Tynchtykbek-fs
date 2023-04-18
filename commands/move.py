import shutil
import os


def move(src_path, dest_path):
    if not os.path.exists(src_path):
        print(f"{src_path} не является допустимым путем к файлу или каталогу.")

    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    shutil.move(src_path, dest_path)
    print('Файл успешно перемещен!')