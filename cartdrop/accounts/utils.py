import os

from django.utils import timezone
from django.contrib.auth import get_user_model

def user_photo_location(instance, filename):
    date = timezone.now()
    path = os.path.join(
        "Users Photos", instance.username, date.year, date.month, date.day, filename
    )
    return path


def create_super_user(username, email, number: None, password):
    User = get_user_model()
    user, created = User.objects.get_or_create(username=username, email=email, number=number, defaults={"is_active": True, "is_staff": True, "is_superuser": True, "is_email_verified": True, "is_number_verified": True})

    if created:
        user.set_password(password)
        user.save()
        message = f"Super with {username} and {email} has been created"
    else:
        message = f"Super with {username} and {email} already exist"
    return message
