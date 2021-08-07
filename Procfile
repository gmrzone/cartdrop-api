web: gunicorn config.wsgi --log-file -
release: python manage.py migrate
release: python manage.py migrate --database=message
release: python manage.py generatedatabase --createadmin