#!/bin/bash

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py generatedatabase --createadmin
python manage.py loaddata json_data/core_new.json
python manage.py loaddata json_data/products.json