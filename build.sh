#!/usr/bin/env bash

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

echo "from django.contrib.auth.models import User;
import os;
username=os.environ.get('DJANGO_SUPERUSER_USERNAME');
email=os.environ.get('DJANGO_SUPERUSER_EMAIL');
password=os.environ.get('DJANGO_SUPERUSER_PASSWORD');
if username and password and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username,email,password)" | python manage.py shell