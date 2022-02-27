import pytest
from django.urls import reverse


@pytest.mark.parametrize("url_name", [("accounts:get_current_user")])
@pytest.mark.django_db
def test_accounts_get_views_status(client, url_name):
    url = reverse(url_name)
    response = client.get(url)
    # response.status_code should be 401 because this vies can only be accessed by authenticated user
    assert response.status_code == 401
