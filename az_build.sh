#!/bin/sh
rm -rf output
python -m venv venv
. ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
ls -l