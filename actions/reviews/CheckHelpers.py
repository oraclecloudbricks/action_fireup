# Copyright (c) 2022 Oracle and/or its affiliates.
# All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl
# CheckHelpers.py
# Description: Includes the logic to check if Static.py includes necessary updates

from actions.utils.helpers.helper import *
import actions.utils.statics.static as static
import re

def check_helpers():

    latest_modified_files = get_modified_files()
    if 'helper.py' in latest_modified_files:
        with open(static.__HELPER_PATHS, 'r') as file:
            file_contents = file.read().rstrip()
            for match in re.finditer('oci.pagination.list_call_get_all_results\(([^)]+)\).data', file_contents):
                s = match.start()
                e = match.end()
                if 'retry_strategy' not in file_contents[s:e]:
                    helper_list = file_contents[s - 60:e]
                    helper_list = ' '.join(helper_list.split())
                    master_json = get_benchmark_dictionary("CHECK_HELPERS_RETRY", "check_helpers",
                                                          "actions/reviews/CheckHelpers.py",
                                                          "Retry Strategy is missing in this: '{}' helper function".format(str(helper_list)), 0)
                    write_json_output(master_json)
                    raise Exception("Retry Strategy is missing in: \n {}".format(str(helper_list)))
            else:
                master_json = get_benchmark_dictionary("CHECK_HELPERS_RETRY", "check_helpers",
                                                       "actions/reviews/CheckHelpers.py",
                                                       "Retry Strategy has been implemented correctly", 1)
                write_json_output(master_json)
                return print("Retry Strategy has been implemented correctly in the helper.py file")

    else:
        master_json = get_benchmark_dictionary("CHECK_HELPERS_RETRY", "check_helpers",
                                               "actions/reviews/CheckHelpers.py",
                                               "helper.py was not modified in this PR. These were the modified files "
                                               "found: {}".format(latest_modified_files), 1)
        write_json_output(master_json)
        return print("helper.py was not modified in this PR. These were the modified files "
                                               "found: {}".format(latest_modified_files))


if __name__ == '__main__':
    check_helpers()