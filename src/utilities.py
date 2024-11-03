from os import path, makedirs

def dir_exists(json_path):
    directory = path.dirname(json_path)
    if not path.exists(directory):
        makedirs(directory)
        print(f"Directory {directory} was created")

def file_exist(json_path):
    dir_exists(json_path)
    if not path.exists(json_path):
        with open(json_path, "w") as f:
            f.write("{}")
        print(f"File {json_path} was created with empty JSON object")