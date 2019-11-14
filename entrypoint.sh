#!/bin/sh -l

ENVIRONMENT_NAME=$1
ENVIRONMENT_PATH=$2
TEMPLATE_PATH=$3
OUTPUT_FILENAME=$4

echo "Building CloudFormation Template"
echo
echo "Environment Name: ${GITHUB_WORKSPACE}/${ENVIRONMENT_NAME}"
echo "Environment Path: ${GITHUB_WORKSPACE}/${ENVIRONMENT_PATH}"
echo "Template Path:    ${GITHUB_WORKSPACE}/${TEMPLATE_PATH}"
echo "Output Filename:  ${GITHUB_WORKSPACE}/${OUTPUT_FILENAME}"

cd /tmp/actions-cloudformation;
ls -l
source ./venv/bin/activate;
python ./build.py "${ENVIRONMENT_NAME}" "${GITHUB_WORKSPACE}/${ENVIRONMENT_PATH}" "${GITHUB_WORKSPACE}/${TEMPLATE_PATH}" "${GITHUB_WORKSPACE}/${OUTPUT_FILENAME}"

echo "Templated Generated: ${GITHUB_WORKSPACE}/${OUTPUT_FILENAME}"
echo
cat "${GITHUB_WORKSPACE}/${OUTPUT_FILENAME}"
