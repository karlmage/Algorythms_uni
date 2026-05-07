import re
from pathlib import Path
project_path = Path(__file__).resolve().parent

def var_search(file_name: str, variable_name: str):
    path_header = str(project_path) + "\\input_data"
    path = f"{path_header}\\{file_name}.txt"

    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
        search_result = re.search(rf"{variable_name}: \d+(, \d+)*", data)
        print(search_result)
    return (re.search(r"\d+(, \d+)*", search_result.group())).group()