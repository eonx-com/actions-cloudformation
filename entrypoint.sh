#!/bin/sh -l

ENVIRONMENT_NAME=$1
ENVIRONMENT_PATH=$2
TEMPLATE_PATH=$3
OUTPUT_FILENAME=$4

echo "Building CloudFormation Template"
echo
echo "Environment Name: ${ENVIRONMENT_NAME}"
echo "Environment Path: ${ENVIRONMENT_PATH}"
echo "Template Path:    ${TEMPLATE_PATH}"
echo "Output Filename:  ${OUTPUT_FILENAME}"

cd /tmp/actions-cloudformation;
ls -l
source ./venv/bin/activate;
python ./build.py "${ENVIRONMENT_NAME}" "${ENVIRONMENT_PATH}" "${TEMPLATE_PATH}" "${GITHUB_WORKSPACE}/${OUTPUT_FILENAME}"

ls -l ${GITHUB_WORKSPACE};
cat "${GITHUB_WORKSPACE}/${OUTPUT_FILENAME}"
