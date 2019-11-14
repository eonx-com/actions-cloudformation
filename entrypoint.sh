#!/bin/sh -l

ACTION=$1
ENVIRONMENT_NAME=$2
ENVIRONMENT_PATH=$3
TEMPLATE_PATH=$4
OUTPUT_FILENAME=$5

if [[ "${ACTION}" = "template_build" ]]; then

  echo "Building CloudFormation Template";
  echo
  echo "Environment Name: ${GITHUB_WORKSPACE}/${ENVIRONMENT_NAME}";
  echo "Environment Path: ${GITHUB_WORKSPACE}/${ENVIRONMENT_PATH}";
  echo "Template Path:    ${GITHUB_WORKSPACE}/${TEMPLATE_PATH}";
  echo "Output Filename:  ${GITHUB_WORKSPACE}/${OUTPUT_FILENAME}";

  cd /tmp/actions-cloudformation;
  ls -l
  source ./venv/bin/activate;
  python ./build.py "${ENVIRONMENT_NAME}" "${GITHUB_WORKSPACE}/${ENVIRONMENT_PATH}" "${GITHUB_WORKSPACE}/${TEMPLATE_PATH}" "${GITHUB_WORKSPACE}/${OUTPUT_FILENAME}"

  echo "Templated Generated: ${GITHUB_WORKSPACE}/${OUTPUT_FILENAME}"
  echo
  cat "${GITHUB_WORKSPACE}/${OUTPUT_FILENAME}"

else

  echo "Unknown action requested: ${ACTION}"
  exit 1;

fi

