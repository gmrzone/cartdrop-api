from django.http.response import HttpResponse
from django.urls import path

from .views import GetCurrentUser, Signup

app_name = "accounts"


urlpatterns = [
    path("get-current-user/", GetCurrentUser.as_view(), name="get_current_user"),
    path("sign-up/", Signup.as_view(), name="signup"),
]
