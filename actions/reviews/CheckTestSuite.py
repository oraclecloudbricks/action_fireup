# Copyright (c) 2022 Oracle and/or its affiliates.
# All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl
# CheckTestSuite.py
# Description: Includes the logic to perform check if test suite was included on PR

from actions.utils.helpers.helper import *
import json
import glob


def check_test_suite():
    files_per_class = get_class_files()
    for key in files_per_class:
        class_files = files_per_class[key]
        test_path = get_test_path(key)
        list_of_tests = glob.glob(test_path)
        if len(list_of_tests) != len(class_files):
            master_json = {
                "Test_Suite_Check": {
                    "action_name": "check_test_suite",
                    "action_path": "actions/check_test_suite.py",
                    "description": "Add a test suite for newly added class: {}".format(key),
                    "passed": 0
                }
            }
            with open('sample.json') as f:
                data = json.load(f)
            data.update(master_json)

            with open('sample.json', 'w') as f:
                json.dump(data, f, indent=2)
            raise Exception("Add a test suite for newly added class: {}".format(key))

    else:
        master_json = {
            "Test_Suite_Check": {
                "action_name": "check_test_suite",
                "action_path": "actions/check_test_suite.py",
                "description": "Test suite has been added successfully",
                "passed": 1
            }
        }
        with open('sample.json') as f:
            data = json.load(f)
        data.update(master_json)

        with open('sample.json', 'w') as f:
            json.dump(data, f, indent=2)
        return print("Test suite has been added successfully")



if __name__ == '__main__':
    check_test_suite()
