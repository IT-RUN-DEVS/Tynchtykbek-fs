import os
import json
import datetime

def snapshot(directory, output_file):
    metadata = {
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'directory': directory,
        'files': []
    }
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            file_metadata = {
                'path': path,
                'size': os.path.getsize(path),
                'created': datetime.datetime.fromtimestamp(os.path.getctime(path)).strftime('%Y-%m-%d %H:%M:%S'),
                'modified': datetime.datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d %H:%M:%S')
            }
            metadata['files'].append(file_metadata)
    with open(output_file, 'w') as f:
        json.dump(metadata, f, indent=4)

    if not os.path.exists(output_file):
        print('Снапшот создан успешно!')
        return

    print(f'Снапшот успешно обновлен!')
