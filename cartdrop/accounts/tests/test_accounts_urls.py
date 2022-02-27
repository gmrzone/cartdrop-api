from django.urls import reverse, resolve
from ..views import *


def test_get_current_user_url():
    url = reverse("accounts:get_current_user")
    resolver = resolve(url)
    assert resolver.func.view_class == GetCurrentUser