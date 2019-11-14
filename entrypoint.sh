#!/bin/sh -l

ENVIRONMENT_NAME=$1
ENVIRONMENT_PATH=$2
TEMPLATE_PATH=$3
OUTPUT_FILENAME=$4

if [[ -d /tmp/actions-cloudformation/venv ]];
  rm -rf /tmp/actions-cloudformation/venv
fi

cd /tmp/actions-cloudformation

python3 -m venv ./venv
source ./venv/bin/activate

pip3 install --upgrade pip3
pip3 install -r ./requirements.txt

./build.py "${ENVIRONMENT_NAME}" "${ENVIRONMENT_PATH}" "${TEMPLATE_PATH}" "${OUTPUT_FILENAME}"
