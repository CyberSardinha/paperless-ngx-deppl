#!/usr/bin/env bash

RUN_DIR=$( dirname -- "$( readlink -f -- "$0"; )"; )
mkdir $RUN_DIR/tmp
chmod -R 777 $RUN_DIR/tmp
echo -n "Setting up virtual environment..."
python -m venv --system-site-packages $RUN_DIR/venv
echo "OK"
source $RUN_DIR/venv/bin/activate
pip install -r $RUN_DIR/requirements.txt
echo -e "\npaperless-ngx-postprocessor setup successful"
