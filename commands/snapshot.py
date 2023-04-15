import os
import shutil

#создание снапшота
def snapshot(source_path, dest_path):
    if not os.path.isfile(source_path):
        raise ValueError(f"{source_path} is not a valid file path.")

    snapshot_dir = os.path.dirname(dest_path)
    if not os.path.exists(snapshot_dir):
        os.makedirs(snapshot_dir)

    shutil.copyfile(source_path, dest_path)


