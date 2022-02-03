# Copyright (c) 2022 Oracle and/or its affiliates.
# All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl
# CheckStatics.py
# Description: Includes the logic to check if Static.py includes necessary updates

from actions.utils.helpers.helper import *
import actions.utils.statics.static as static
import re

def check_statics():

    rp_number = get_review_number()
    latest_modified_files = get_modified_files()
    if 'Statics.py' in latest_modified_files:
        file = open(static.__STATICS_PATH).read().splitlines()
        for index, line in enumerate(file):
            if re.findall(str(rp_number) + '\\b', line):
                file_needed = file[index:index + 8]
                if re.findall("'sub_area': '',", file_needed[3]):
                    master_json = get_benchmark_dictionary("CHECK_STATICS", "check_statics", "actions/reviews/CheckStatics.py",
                                                           "The sub_area of {} in Statics.py is missing'.format(rp_number)", 0)
                    write_json_output(master_json)
                    raise Exception('The sub_area of {} in Statics.py is missing'.format(rp_number))
                if re.findall("'review_point': '',", file_needed[4]):
                    master_json = get_benchmark_dictionary("CHECK_STATICS", "check_statics", "actions/reviews/CheckStatics.py",
                                                           "The review_point section of {} in Statics.py is missing".format(rp_number), 0)
                    write_json_output(master_json)
                    raise Exception('The review_point section of {} in Statics.py is missing'.format(rp_number))
                if re.findall("'success_criteria': '',", file_needed[5]):
                    master_json = get_benchmark_dictionary("CHECK_STATICS", "check_statics", "actions/reviews/CheckStatics.py",
                                                           "The success_criteria section of {} in Statics.py is missing".format(rp_number), 0)
                    write_json_output(master_json)
                    raise Exception('The success_criteria section of {} in Statics.py is missing'.format(rp_number))
                if ": []," in file_needed[6]:
                    master_json = get_benchmark_dictionary("CHECK_STATICS", "check_statics", "actions/reviews/CheckStatics.py",
                                                           "The fireup_items section of {} in Statics.py is missing".format(rp_number), 0)
                    write_json_output(master_json)
                    raise Exception('The fireup_items section of {} in Statics.py is missing'.format(rp_number))
                else:
                    master_json = get_benchmark_dictionary("CHECK_STATICS", "check_statics", "actions/reviews/CheckStatics.py",
                                                           "The {} section in Statics.py has been filled accordingly".format(rp_number), 1)
                    write_json_output(master_json)
                    return print('The {} section in Statics.py has been filled accordingly'.format(rp_number))
    else:
        master_json = get_benchmark_dictionary("CHECK_STATICS", "check_statics", "actions/reviews/CheckStatics.py",
                                               "Statics.py has not been modified for this review point. These were "
                                               "the modified files found: {}".format(
                                                   latest_modified_files), 0)
        write_json_output(master_json)
        return print( "Statics.py has not been modified for: {pos1}. These were the modified files found: {pos2}".format(pos1 = rp_number,pos2 = latest_modified_files))


if __name__ == '__main__':
    check_statics()