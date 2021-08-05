import os
from django.utils import timezone

def user_photo_location(instance, filename):
    date = timezone.now()
    path = os.path.join("Users Photos", instance.username, date.year, date.month, date.day, filename)
    return path