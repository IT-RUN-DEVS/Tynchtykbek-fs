import shutil

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