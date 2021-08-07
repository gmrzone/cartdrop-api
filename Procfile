release: python manage.py migrate
web: gunicorn config.wsgi --log-file -
release: python manage.py generatedatabase --createadmin