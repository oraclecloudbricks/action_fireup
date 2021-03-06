# Copyright (c) 2022 Oracle and/or its affiliates.
# !/usr/bin/env bash
# All rights reserved. The Universal Permissive License (UPL), Version 1.0 as shown at http://oss.oracle.com/licenses/upl
# action_builder.sh 
#
# Purpose: Main module for building the action. This script serves as an orchestrator for actions processed by the action_builder.sh

echo "Running Action Builder"
echo ""

cd ../../

string=$INPUT_BRANCH_NAME
reqsubstr='feature'
if [ -z "${string##*$reqsubstr*}" ] ;
then
  echo ""
  python3 -m actions.reviews.CheckClassReadme
  echo ""
  python3 -m actions.reviews.CheckTestSuite
  echo ""
  python3 -m actions.reviews.CheckHeaders
  echo ""
  python3 -m actions.reviews.CheckStatics
  echo ""
  python3 -m actions.reviews.CheckPRTests
  echo ""
  python3 -m actions.reviews.CheckHelpers
  echo ""
else
  echo ""
  python3 -m actions.reviews.CheckPRTests
fi

cp results.json github/workspace/results.json
