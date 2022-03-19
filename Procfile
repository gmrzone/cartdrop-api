web: gunicorn config.wsgi --log-file -
release: python manage.py generate_data --createadmin
# release: python manage.py migrate && python manage.py generatedatabase --create-admin && python manage.py loaddata json_data/core_latest.json && python manage.py loaddata json_data/product_latest.json