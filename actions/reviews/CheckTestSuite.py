# Copyright (c) 2022 Oracle and/or its affiliates.
# All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl
# CheckTestSuite.py
# Description: Includes the logic to perform check if test suite was included on PR

from actions.utils.helpers.helper import *
import glob


def check_test_suite():
    files_per_class = get_class_files()
    for key in files_per_class:
        class_files = files_per_class[key]
        test_path = get_test_path(key)
        list_of_tests = glob.glob(test_path)
        if len(list_of_tests) != len(class_files):
            master_json = get_benchmark_dictionary("CHECK_TEST_SUITE", "check_test_suite", "actions/CheckTestSuite.py",
                                                   "Add a test suite for newly added class: {}".format(key), 0)
            write_json_output(master_json)
            raise Exception("Add a test suite for newly added class: {}".format(key))

    else:
        master_json = get_benchmark_dictionary("CHECK_TEST_SUITE", "check_test_suite", "actions/CheckTestSuite.py",
                                               "Test suite has been added successfully", 1)
        write_json_output(master_json)
        return print("Test suite has been added successfully")


if __name__ == '__main__':
    check_test_suite()
