# Copyright (c) 2022 Oracle and/or its affiliates.
# All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl
# HELPER.py
# Description: Includes all helper functions used in project

import json
import os


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
            master_json = get_benchmark_dictionary("HELPER", "get_latest_added_class_files", "actions/utils/helpers/helper.py",
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
    branch_name = get_branch_name().lower()
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