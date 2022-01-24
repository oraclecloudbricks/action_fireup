#!/bin/sh
echo "Running Action Builder"
echo ""
python3 ../../actions/check_class_readme.py
python3 ../../actions/check_test_suite.py
cp ../../sample.json .