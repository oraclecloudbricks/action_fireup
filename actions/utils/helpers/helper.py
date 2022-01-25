# Copyright (c) 2022 Oracle and/or its affiliates.
# All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl
# HELPER.py
# Description: Includes all helper functions used in project
import actions.utils.statics.static as static
import glob
import json
import os


def get_class_files():
    files_per_class = {}
    for path in static.__PATHS:
        list_of_files = glob.glob(path)
        class_name = path.split('/')[3]
        files_per_class[class_name] = list_of_files
    return files_per_class


def get_benchmark_dictionary(entry, action_name, action_path, description, status):
    return {
        str(entry): {
            "action_name": action_name,
            "action_path": action_path,
            "description": description,
            "passed": status
        }
    }


def write_json_output(master_json):
    if not os.path.exists('results.json'):
        with open('results.json', mode='w') as f:
            f.write(json.dumps(master_json, indent=2))

    else:
        with open('results.json') as f:
            data = json.load(f)
        data.update(master_json)
        with open('results.json', 'w') as f:
            json.dump(data, f, indent=2)


def get_readme_path(files_per_class_key):
    readme_path = 'github/workspace/classes/' + str(files_per_class_key) + '/README.md'
    return readme_path


def get_test_path(files_per_class_key):
    test_path = 'github/workspace/test/' + str(files_per_class_key) + '/[A-Za-z]*py'
    return test_path