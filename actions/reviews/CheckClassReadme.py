# Copyright (c) 2022 Oracle and/or its affiliates.
# All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl
# CheckClassReadme.py
# Description: Includes the logic to check if Readme has been updated with corresponding class during a PR

from actions.utils.helpers.helper import *
import os


def check_readme():
    files_per_class = get_class_files()

    for key in files_per_class:
        class_files = files_per_class[key]
        readme_path = get_readme_path(key)
        readme_items = []
        if os.path.exists(readme_path):
            with open(readme_path) as f:
                for line in f:
                    if '.py' in line:
                        name = line.split('.py')[0].split('[')[1]
                        readme_items.append(name)
        if len(readme_items) != len(class_files):
            master_json = get_benchmark_dictionary("CHECK_README", "check_readme", "actions/CheckClassReadme.py",
                                                   "Update {} to match the latest class update".format(readme_path), 0)
            write_json_output(master_json)
            raise Exception("Update {} to match the latest class update".format(readme_path))
    else:
        master_json = get_benchmark_dictionary("CHECK_README", "check_readme", "actions/CheckClassReadme.py",
                                               "README.md file: {} is up to date".format(readme_path), 1)
        write_json_output(master_json)
        return print("README.md file: {} is up to date".format(readme_path))


if __name__ == '__main__':
    check_readme()
