import os
from pathlib import Path
BASE_UTILS_DIR = Path(__file__).resolve().parent.parent

def file_list(directory_path : str):
    content = os.listdir(directory_path)
    return content

def get_raw(directory_path : str, file_name : str):
    file_path = os.path.join('{}/{}'.format(directory_path,file_name))
    with open(file_path, 'r',encoding='utf8') as file:
        data = file.read().rstrip()
    return data
