# Copyright (c) 2022 Oracle and/or its affiliates.
# All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl
# HELPER.py
# Description: Includes all helper functions used in project
import actions.utils.statics.static as static
import glob


def get_class_files():
    files_per_class = {}
    for path in static.__PATHS:
        list_of_files = glob.glob(path)
        class_name = path.split('/')[3]
        files_per_class[class_name] = list_of_files
    return files_per_class


def get_readme_path(files_per_class_key):
    readme_path = 'github/workspace/classes/'+ str(files_per_class_key) + '/README.md'
    return readme_path


def get_test_path(files_per_class_key):
    test_path = 'github/workspace/test/' + str(files_per_class_key) + '/[A-Za-z]*py'
    return test_path
