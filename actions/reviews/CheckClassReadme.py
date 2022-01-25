# Copyright (c) 2022 Oracle and/or its affiliates.
# All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl
# CheckClassReadme.py
# Description: Includes the logic to check if Readme has been updated with corresponding class during a PR

from actions.utils.helpers.helper import *
import json
import os

def check_readme():

    files_per_class = get_class_files()

    for key in files_per_class:
        class_files = files_per_class[key]
        readme_path = get_readme_path(key)
        readme_items = []
        if os.path.exists(readme_path):
            with open(readme_path) as f:
                for line in f:
                    if '.py' in line:
                        name = line.split('.py')[0].split('[')[1]
                        readme_items.append(name)
        if len(readme_items) != len(class_files):
            master_json = {
                "README_check": {
                    "action_name": "check_readme",
                    "action_path": "actions/check_class_readme.py",
                    "description": "Update {} to match the latest class update".format(readme_path),
                    "passed": 0
                }
            }
            with open('sample.json', mode='w') as f:
                f.write(json.dumps(master_json, indent=2))
            raise Exception("Update {} to match the latest class update".format(readme_path))
    else:
        master_json = {
            "README_check": {
                "action_name": "check_readme",
                "action_path": "actions/check_class_readme.py",
                "description": "README.md file: {} is up to date".format(readme_path),
                "passed": 1
            }
        }
        with open('sample.json', mode='w') as f:
            f.write(json.dumps(master_json, indent=2))
        return print("README.md file: {} is up to date".format(readme_path))


if __name__ == '__main__':
    check_readme()