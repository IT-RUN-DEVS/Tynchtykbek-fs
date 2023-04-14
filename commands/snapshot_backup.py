import os
import shutil
import datetime

#создание снапшота
def create_file_snapshot(source_path, dest_path):
    if not os.path.isfile(source_path):
        raise ValueError(f"{source_path} is not a valid file path.")

    snapshot_dir = os.path.dirname(dest_path)
    if not os.path.exists(snapshot_dir):
        os.makedirs(snapshot_dir)

    shutil.copyfile(source_path, dest_path)


#бэкап
def create_backup(source_path, backup_dir):
    if not os.path.exists(source_path):
        raise ValueError(f"{source_path} is not a valid file or directory path.")

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
