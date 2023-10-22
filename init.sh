#!/usr/bin/bash

python web_app/manage.py makemigrations
python web_app/manage.py migrate
python web_app/manage.py runserver
