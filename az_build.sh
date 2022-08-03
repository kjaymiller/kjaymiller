#!/bin/sh
rm -rf output
python -m venv venv
. venv/bin/activate
pip install --user --upgrade pip
pip install --user -r requirements.txt