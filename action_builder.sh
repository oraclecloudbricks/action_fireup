# Copyright (c) 2022 Oracle and/or its affiliates.
# !/usr/bin/env bash
# All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl
# action_builder.sh 
#
# Purpose: Main module for building the action. This script serves as an orchestrator for actions processed by the action_builder.sh

echo "Running Action Builder"
echo ""
cd ../../
python3 -m actions.reviews.CheckClassReadme
echo ""
python3 -m actions.reviews.CheckTestSuite
echo ""
python3 -m actions.reviews.CheckStatics
echo ""
cp results.json github/workspace/results.json