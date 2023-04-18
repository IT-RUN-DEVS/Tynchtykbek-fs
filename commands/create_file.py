import os

#cоздание нового файла
def create_file(file_name):
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            file.write('')
        print(f'Файл {file_name} создан успешно!')





