#!/bin/bash

python manage.py wait_for_db
python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input

exec "$@"
