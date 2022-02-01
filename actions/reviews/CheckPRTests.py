# Copyright (c) 2022 Oracle and/or its affiliates.
# All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl
# CheckPRTests.py
# Description: Includes the logic to check if the tests included in the PR have all passed

from actions.utils.helpers.helper import *
import re


def check_pr_tests():
    pr_body = get_pr_body()
    if re.findall('collected', pr_body):
        for match in re.finditer('collected', pr_body):
            num_tests = pr_body[match.start() + 10:match.end() + 3]
            counter = 0
            for match in re.finditer('PASSED', pr_body):
                test_info = pr_body[match.start():match.end() + 7]
                counter += 1
                if counter == int(num_tests):
                    print("All tests included in the PR have PASSED")
                    master_json = get_benchmark_dictionary("CHECK_PR_TESTS", "check_pr_tests",
                                                           "actions/reviews/CheckPRTests.py",
                                                           "All tests included in the PR have PASSED", 1)
                    write_json_output(master_json)

    elif re.findall('(?i)(passed)', pr_body):
        print("All tests included in the PR seem to have PASSED but the PR does not conform to the structure required")
        master_json = get_benchmark_dictionary("CHECK_PR_TESTS", "check_pr_tests", "actions/reviews/CheckPRTests.py",
                                               "All tests included in the PR seem to have PASSED but the PR opened "
                                               "does not conform to the structure required", 0)
        write_json_output(master_json)
    elif re.findall('(?i)(failed)', pr_body):
        for match in re.finditer('(?i)(failed)', pr_body):
            failed_test = pr_body[match.start() - 30:match.end()]
            print("A test or more seem to be failing. See: {}".format(failed_test))
            master_json = get_benchmark_dictionary("CHECK_PR_TESTS", "check_pr_tests",
                                                   "actions/reviews/CheckPRTests.py",
                                                   "A test or more seem to be failing. See: {}".format(failed_test), 0)
            write_json_output(master_json)
    else:
        print("There seems to be no test suite included in this PR")
        master_json = get_benchmark_dictionary("CHECK_PR_TESTS", "check_pr_tests",
                                               "actions/reviews/CheckPRTests.py",
                                               "There seems to be no test suite included in this PR", 0)
        write_json_output(master_json)


if __name__ == '__main__':
    check_pr_tests()
