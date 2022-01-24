
import utils.statics.static as static
import glob
import os

def get_files_and_paths():
    python_files = []
    python_file_paths = []
    for path in static.__PATHS:
        list_of_files = glob.glob(path)
        for file in list_of_files:
            if '.py' in file and '__init__.py' not in file:
                python_files.append(file)
                python_file_paths.append((file, path))
    return python_files, python_file_paths

def get_latest_file(python_files):
    latest_file = max(python_files, key=os.path.getctime)
    return latest_file

def get_class_name(latest_file):
    class_name = latest_file.split('/')[1]
    return class_name

def get_class_path(latest_file):
    class_path = '/'+latest_file.split('/')[1] + '/'
    return class_path