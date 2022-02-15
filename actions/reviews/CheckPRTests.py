# Copyright (c) 2022 Oracle and/or its affiliates.
# All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl
# CheckPRTests.py
# Description: Includes the logic to check if the tests included in the PR have all passed

from actions.utils.helpers.helper import *
import re

def check_pr_tests():
    branch_name = get_branch_name()
    if 'feature' in branch_name:
        check_tests()
    added_files = get_latest_added_files()
    modified_files = get_modified_files()
    if 'feature' not in branch_name:
        remaining_files = []
        for modified_file in modified_files.split():
            if 'Statics.py' not in modified_file and '.md' not in modified_file and '.yml' not in modified_file:
                remaining_files.append(modified_file)
        for added_file in added_files.split():
            if 'Statics.py' not in added_file and '.md' not in added_file and '.yml' not in added_file:
                remaining_files.append(added_file)

        if len(remaining_files) != 0:
            check_tests()
        else:
            master_json = get_benchmark_dictionary("CHECK_PR_TESTS", "check_pr_tests", "actions/reviews/CheckPRTests.py",
                                            "This PR does not require testing based on the files which have been added: {pos1} and modified: {pos2}".format(pos1=added_files, pos2=modified_files), 1)
            write_json_output(master_json)
            return print("This PR does not require testing based on the files which have been added: {pos1} and modified: {pos2}".format(pos1=added_files, pos2=modified_files))

if __name__ == '__main__':
    check_pr_tests()