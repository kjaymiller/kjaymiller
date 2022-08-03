#!/bin/sh
rm -rf output
pip install --upgrade pip
pip install -r requirements.txt
python routes.py

npx install tailwindcss
npx tailwindcss -o output/static/css/tailwind.css --minify
