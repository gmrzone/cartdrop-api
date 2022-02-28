import os

from django.contrib.auth import get_user_model
from django.utils import timezone


def user_photo_location(instance, filename):
    date = timezone.now()
    path = os.path.join(
        "Users Photos", instance.username, date.year, date.month, date.day, filename
    )
    return path


def create_super_user(username, email, number: None, password):
    User = get_user_model()
    user, created = User.objects.get_or_create(
        username=username,
        email=email,
        number=number,
        defaults={
            "is_active": True,
            "is_staff": True,
            "is_superuser": True,
            "is_email_verified": True,
            "is_number_verified": True,
        },
    )

    if created:
        user.set_password(password)
        user.save()
        message = (
            f"Super User with username: {username} and email: {email} has been created"
        )
    else:
        message = (
            f"Super User with username: {username} and email: {email} already exist"
        )
    return message


def create_normal_user(username, email, number: None, password):

    User = get_user_model()
    user, created = User.objects.get_or_create(
        username=username,
        email=email,
        number=number,
        defaults={
            "is_active": True,
            "is_staff": False,
            "is_superuser": False,
            "is_email_verified": True,
            "is_number_verified": True,
        },
    )

    if created:
        user.set_password(password)
        user.save()
        message = (
            f"Normal User with username: {username} and email: {email} has been created"
        )
    else:
        message = (
            f"Normal User with username: {username} and email: {email} already exist"
        )
    return message
