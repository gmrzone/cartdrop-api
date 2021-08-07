#!/bin/bash

release: python manage.py migrate
release: python manage.py generatedatabase --createadmin