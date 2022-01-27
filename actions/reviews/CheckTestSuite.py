# Copyright (c) 2022 Oracle and/or its affiliates.
# All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl
# CheckTestSuite.py
# Description: Includes the logic to perform check if test suite was included on PR

from actions.utils.helpers.helper import *

def check_test_suite():
    latest_added_files = get_latest_added_files()
    if 'test/' in latest_added_files:
        test_added = latest_added_files.split(' ')[0]
        master_json = get_benchmark_dictionary("CHECK_TEST_SUITE", "check_test_suite", "actions/CheckTestSuite.py",
                                               "Test suite has been added successfully".format(test_added), 1)
        write_json_output(master_json)
        return print("Test suite has been added successfully: {}".format(test_added))
    else:
        if 'classes/' in latest_added_files:
            latest_file_path = latest_added_files.split(' ')[0]
            master_json = get_benchmark_dictionary("CHECK_TEST_SUITE", "check_test_suite", "actions/CheckTestSuite.py",
                                                   "Add a test suite for newly added class: {}".format(
                                                       latest_file_path), 0)
            write_json_output(master_json)
            raise Exception("Add a test suite for newly added class: {}".format(latest_file_path))
        else:
            master_json = get_benchmark_dictionary("CHECK_TEST_SUITE", "check_test_suite", "actions/CheckTestSuite.py",
                                                   "No new Python Class was added in this PR. These were the latest "
                                                   "files added:".format(latest_added_files), 2)
            write_json_output(master_json)
            raise Exception('No new Python Class was added in this commit')


if __name__ == '__main__':
    check_test_suite()
