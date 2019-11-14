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

./build.py "${ENVIRONMENT_NAME}" "${ENVIRONMENT_PATH}" "${TEMPLATE_PATH}" "${OUTPUT_FILENAME}"

$(cat ${OUTPUT_FILENAME})1