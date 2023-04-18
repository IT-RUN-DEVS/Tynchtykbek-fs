import datetime
import os
import shutil


def backup(source_path: str, backup_dir: str) -> str:
    if not os.path.exists(source_path):
        print(f"{source_path} не является допустимым путем к файлу или директории")
        return

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    if os.path.isfile(source_path):
        filename = os.path.basename(source_path)
        backup_filename = f"{filename}.{timestamp}.bak"
        backup_path = os.path.join(backup_dir, backup_filename)
        shutil.copy2(source_path, backup_path)

    elif os.path.isdir(source_path):
        dirname = os.path.basename(source_path)
        backup_dirname = f"{dirname}.{timestamp}.bak"
        backup_path = os.path.join(backup_dir, backup_dirname)
        shutil.copytree(source_path, backup_path)

    print('Резервная копия успешно создана!')