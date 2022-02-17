# Copyright (c) 2022 Oracle and/or its affiliates.
# All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl
# HELPER.py
# Description: Includes all helper functions used in project
import actions.utils.statics.static as static
import glob
import json
import os
import re


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


def get_latest_added_files():
    latest_files = os.getenv('INPUT_FILES_ADDED')
    return latest_files


def get_latest_added_class_files():
    latest_files = get_latest_added_files()
    if 'classes/' in latest_files:
        latest_added_files = latest_files.split(' ')
        for latest_added_file in latest_added_files:
            if 'classes/' in latest_added_file:
                return latest_added_file
        else:
            master_json = get_benchmark_dictionary("HELPER", "get_latest_added_class_files", "actions/untils/helpers/helper.py",
                                                   "No new Python Class was added in this PR. These were the latest "
                                                   "files added:".format(latest_added_files), 2)
            write_json_output(master_json)
            raise Exception('No new Python Class was added in this commit')


def get_latest_added_class_file_path(latest_added_file):
    test_path = 'github/workspace/' + str(latest_added_file)
    return test_path


def get_modified_files():
    modified_files = os.getenv('INPUT_FILES_MODIFIED')
    return modified_files


def get_pr_body():
    pr_body = os.getenv('INPUT_PR_BODY')
    return pr_body


def get_branch_name():
    branch_name = os.getenv('INPUT_BRANCH_NAME')
    return branch_name


def get_review_number():
    branch_name = get_branch_name()
    branch_name = branch_name.lower()
    rp_number = branch_name.split('feature/')[1]
    if '.' in rp_number:
        rp_number = rp_number.replace('.', '_')
    if len(rp_number) > 10:
        if rp_number[7].isalpha():
            rp_number = rp_number[:6]
            return rp_number
        elif rp_number[9].isalpha():
            if not rp_number[8].isalnum():
                rp_number = rp_number[:8]
                if not rp_number[-2].isalnum():
                    rp_number = rp_number[:6] + '' + rp_number[7:]
                    return rp_number
            else:
                rp_number = rp_number[:8]
                if not rp_number[-1].isalnum():
                    rp_number = rp_number[:7]
                    return rp_number
                if not rp_number[-2].isalnum():
                    rp_number = rp_number[:6] + '' + rp_number[7:]
                    return rp_number
    else:
        return rp_number

def check_tests():
    if os.path.isfile(static.__TEST_LOG_PATH):
        log_file = open(static.__TEST_LOG_PATH).read()
        for match in re.finditer('collected', log_file):
            num_tests = log_file[match.start() + 10:match.end() + 3]
            counter = 0
            for match in re.finditer('PASSED', log_file):
                test_info = log_file[match.start():match.end() + 7]
                counter += 1
            if counter == int(num_tests):
                master_json = get_benchmark_dictionary("CHECK_PR_TESTS", "check_pr_tests",
                                                        "actions/reviews/CheckPRTests.py",
                                                        "All tests included in the logfile have PASSED", 1)
                write_json_output(master_json)
                return print("All tests included in the PR have PASSED")

            else:
                master_json = get_benchmark_dictionary("CHECK_PR_TESTS", "check_pr_tests",
                                                    "actions/reviews/CheckPRTests.py",
                                                    "A test or more included in the logfile seem to be "
                                                    "failing. {pos1} Tests were included of which {pos2} "
                                                    "passed".format(pos1=str(num_tests), pos2=str(counter)),
                                                    0)
                write_json_output(master_json)
                raise Exception("A test or more included in the logfile seem to be failing. '{pos1}' Tests were included of "
                    "which '{pos2}' passed".format(pos1=str(num_tests), pos2=str(counter)))
    else: 
        master_json = get_benchmark_dictionary("CHECK_PR_TESTS", "check_pr_tests", "actions/reviews/CheckPRTests.py",
                                            "The log file containing the tests was not included in this Pull Request. Please run the tests and add it", 0)
        write_json_output(master_json)
        raise Exception ("The logfile containing the tests was not included in this Pull Request. Please run the tests and add it")  