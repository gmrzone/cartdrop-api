import numbers
from urllib import response
from webbrowser import get
import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model


@pytest.mark.parametrize("url_name", [("accounts:get_current_user")])
@pytest.mark.django_db
def test_accounts_get_views_status(client, url_name):
    url = reverse(url_name)
    response = client.get(url)
    # response.status_code should be 401 because this vies can only be accessed by authenticated user
    assert response.status_code == 401


@pytest.mark.django_db
def test_signup_view_with_proper_data(client):
    url = reverse("accounts:signup")
    User = get_user_model()
    # With proper data response status should be 200
    data = {
        "username": "AfzalSaiyed",
        "number": "9220976696",
        "email": "saiyedafzalgz@gmail.com",
        "password": "password123",
        "confirm_password": "password123",
    }
    assert User.objects.count() == 0
    response = client.post(url, data=data)
    assert User.objects.count() == 1
    assert response.status_code == 200


@pytest.mark.django_db
def test_signup_view_different_password_and_confirm_password(client):
    url = reverse("accounts:signup")
    User = get_user_model()
    # Improper data both password dont match so response status should be 403
    data = {
        "username": "AfzalSaiyed",
        "number": "9220976696",
        "email": "saiyedafzalgz@gmail.com",
        "password": "password123",
        "confirm_password": "123password",
    }
    assert User.objects.count() == 0
    response = client.post(url, data=data)
    assert User.objects.count() == 0
    assert response.status_code == 403


@pytest.mark.django_db
def test_signup_view_without_username(client):
    # Creating a user without username should return 403. error
    data = {
        "number": "9220976696",
        "email": "saiyedafzalgz@gmail.com",
        "password": "password123",
        "confirm_password": "password123",
    }
    url = reverse("accounts:signup")
    response = client.post(url, data=data)
    assert response.status_code == 403


@pytest.mark.django_db
def test_signup_view_without_email(client):
    # Creating a user without email should return 403. error
    data = {
        "username": "AfzalSaiyed",
        "number": "9220976696",
        "password": "password123",
        "confirm_password": "password123",
    }
    url = reverse("accounts:signup")
    response = client.post(url, data=data)
    assert response.status_code == 403
