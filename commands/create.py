import os

#cоздание нового файла
def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write('')
        print(f'File {file_name} created successfully!')
    except Exception as e:
        print(f'Error creating file {file_name}: {e}')


#создание новой директории
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory {path} created.")
    else:
        print(f"Directory {path} already exists.")
