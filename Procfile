web: gunicorn config.wsgi --log-file -
release: python manage.py migrate && python manage.py generatedatabase --createadmin && python manage.py loaddata json_data/core.json