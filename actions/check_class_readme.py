import os.path
import glob
import json


def check_read_me():

    class_path = None
    readme_path = None
    paths = ['classes/securitycompliance/*', 'classes/reliabilityresilience/*', 'classes/performancecost/*',
             'classes/opsefficiency/*']

    python_files = []
    python_file_paths = []
    for path in paths:
        list_of_files = glob.glob(path)
        for file in list_of_files:
            if '.py' in file and '__init__.py' not in file:
                python_files.append(file)
                python_file_paths.append((file, path))

    latest_file = max(python_files, key=os.path.getctime)

    text_list = []

    for pairs in python_file_paths:
        if latest_file in pairs:
            index = python_file_paths.index(pairs)
            class_path = python_file_paths[index][1]
            readme_path = class_path.split('/*')[0] + '/README.md'
            if not os.path.exists(readme_path):
                master_json = {
                    "README_check": {
                        "action_name": "check_readme",
                        "action_path": "actions/check_class_readme.py",
                        "description": "The following path: {} has no README file".format(readme_path),
                        "passed": 0
                    }
                }
                with open('../../../sample.json', mode='w') as f:
                    f.write(json.dumps(master_json, indent=2))
                raise Exception("The following path: {} has no README file".format(readme_path))

            with open(readme_path) as f:
                for line in f:
                    if '.py' in line:
                        name = line.split('.py')[0].split('[')[1]
                        text_list.append(name)
    class_files = []
    for pairs in python_file_paths:
        if class_path in pairs:
            class_files.append(pairs[0])

    if len(text_list) != len(class_files):
        master_json = {
            "README_check": {
                "action_name": "check_readme",
                "action_path": "actions/check_class_readme.py",
                "description": "Update {} to match the latest class update".format(readme_path),
                "passed": 0
            }
        }
        with open('../../../sample.json', mode='w') as f:
            f.write(json.dumps(master_json, indent=2))
        raise Exception("Update {} to match the latest class update".format(readme_path))

    else:
        master_json = {
            "README_check": {
                "action_name": "check_readme",
                "action_path": "actions/check_class_readme.py",
                "description": "README.md file in {} is up to date".format(class_path),
                "passed": 1
            }
        }
        with open('../../../sample.json', mode='w') as f:
            f.write(json.dumps(master_json, indent=2))
        return print("README.md file in {} is up to date".format(class_path))


if __name__ == '__main__':
    check_read_me()

