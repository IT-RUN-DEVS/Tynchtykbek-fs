import os

def init(root_dir, subdirs=[], files={}):
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)

    else:
        print('Такая директория уже существует!')

    for subdir in subdirs:
        subdir_path = os.path.join(root_dir, subdir)
        if not os.path.exists(subdir_path):
            os.makedirs(subdir_path)

    for filename, contents in files.items():
        filepath = os.path.join(root_dir, filename)
        with open(filepath, 'w') as f:
            f.write(contents)

    print('Директория инициализирована успешно')