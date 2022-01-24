# Copyright (c) 2022 Oracle and/or its affiliates.
# All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl
# CheckTestSuite.py
# Description: Includes the logic to perform if test suite was included on PR

import os.path
import glob
import json
import utils.helpers.helper as helper
import utils.statics.static as static


def check_test_suite():
    target_dir = None
    class_dir_files = []    

    python_files, python_file_paths = helper.get_files_and_paths()
      

    latest_file = helper.get_latest_file(python_files)

    class_name = helper.get_class_name(latest_file)
    class_path = helper.get_class_path(latest_file)

    class_files = []
    for pairs in python_file_paths:
        if class_path in pairs[0]:
            class_files.append(pairs[0])

    test_sub_dirs = os.listdir('test/')
    for sub_dir in test_sub_dirs:
        if class_name in sub_dir:
            target_dir = 'test/' +str(sub_dir) + '/*'

    target_dir_files = glob.glob(target_dir)

    if len(class_dir_files) != len(target_dir_files):
        master_json = {
            "Test_Suite_Check": {
                "action_name": "check_test_suite",
                "action_path": "actions/check_test_suite.py",
                "description": "Add a test suite for newly added class: {}".format(latest_file),
                "passed": 0
            }
        }
        with open('../../../sample.json') as f:
            data = json.load(f)
        data.update(master_json)

        with open('../../../sample.json', 'w') as f:
            json.dump(data, f, indent=2)
        raise Exception("Add a test suite for newly added class: {}".format(latest_file))
    else:
        data = {
            "Test_Suite_Check": {
                "action_name": "check_test_suite",
                "action_path": "actions/check_test_suite.py",
                "description": "Test suite has been added successfully",
                "passed": 1
            }
        }
        with open('../../../sample.json', mode='a') as f:
            f.write(json.dumps(data, indent=2))
        return print("Test suite has been added successfully")

if __name__ == '__main__':
    check_test_suite()
