import os
import shutil
import tarfile

#создание снапшота
def create_snapshot(snapshot_name, root_path):
    with tarfile.open(snapshot_name, "w:gz") as tar:
        tar.add(root_path, arcname=os.path.basename(root_path))


#бэкап
def backup(source_dir, dest_dir):
    shutil.copytree(source_dir, dest_dir)
