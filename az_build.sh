#!/bin/sh
npx tailwindcss -i ./static/css/pre/tailwind.css build -o static/css/tailwind.css
rm -rf output
pip install --upgrade pip
pip install -r requirements.txt
python routes.py