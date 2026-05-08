import re
from pathlib import Path
project_path = Path(__file__).resolve().parent
path_header = str(project_path) + "\\input_data"

def get_sets(file_name: str):
    path = f"{path_header}\\{file_name}.txt"

    found_sets = []

    with open(path, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            search_result = re.search(rf"\d+(,\d+)*", i)
            found_sets.append(search_result.group().split(','))

    print(found_sets)
    return found_sets
