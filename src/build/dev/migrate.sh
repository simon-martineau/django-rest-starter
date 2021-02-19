#!/usr/bin/env bash

python3 manage.py wait_for_db
python3 manage.py makemigrations
python3 manage.py migrate --no-input