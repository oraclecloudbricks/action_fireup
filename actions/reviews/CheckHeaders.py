# Copyright (c) 2022 Oracle and/or its affiliates.
# All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl
# CheckHeaders.py
# Description: Includes the logic to check if Headers of each class have the correct labelling

from actions.utils.helpers.helper import *


def check_header():

    latest_class_file = get_latest_added_class_files()
    latest_class_file_path = get_latest_added_class_file_path(latest_class_file)
    file_name = latest_class_file.split('/')[2].split('.')[0]

    file = open(latest_class_file_path).read().splitlines()
    for index, line in enumerate(file):
        if index == 2:
            header_info = file[index:index + 2]
            for info in header_info:
                if file_name in info:
                    print('This file: {} has the right headers!'.format(latest_class_file))
                    master_json = get_benchmark_dictionary("CHECK_HEADER", "check_header", "actions/CheckHeaders.py",
                                                           'This file: {} has the right headers!'.format(latest_class_file), 1)
                    write_json_output(master_json)
                else:
                    master_json = get_benchmark_dictionary("CHECK_HEADER", "check_header", "actions/CheckHeaders.py",
                                                           "{pos1} contains the wrong headers: {pos2} ".format(pos1=latest_class_file, pos2=file[index:index + 2]), 0)
                    write_json_output(master_json)
                    raise Exception(' {pos1} contains the wrong headers: {pos2} '.format(
                        pos1=latest_class_file, pos2=file[index:index + 2]))


if __name__ == '__main__':
    check_header()
