import os

#cоздание нового файла
def create_file(file_name):
    if os.path.exists(file_name):
        print('Файл с таким именем уже существует! Задайте другое имя!')
        return
    try:
        with open(file_name, 'w') as file:
            file.write('')
        print(f'File {file_name} created successfully!')
    except Exception as e:
        print(f'Error creating file {file_name}: {e}')


