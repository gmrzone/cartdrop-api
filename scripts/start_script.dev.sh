#!/bin/bash


python manage.py migrate --no-input
python manage.py generatedatabase --createadmin