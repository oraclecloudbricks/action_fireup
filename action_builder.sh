# Copyright (c) 2022 Oracle and/or its affiliates.
# !/usr/bin/env bash
# All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl
# action_builder.sh 
#
# Purpose: Main module for building the action. This script serves as an orchestrator for actions processed by the action_builder.sh

echo "Running Action Builder"
echo ""
python3 ../../actions/reviews/CheckClassReadme.py
python3 ../../actions/reviews/CheckTestSuite.py
cp ../../sample.json .