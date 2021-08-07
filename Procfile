web: gunicorn config.wsgi --log-file -
release: python manage.py migrate && ython manage.py generatedatabase --createadmin