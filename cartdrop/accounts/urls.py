from django.http.response import HttpResponse
from django.urls import path

app_name = "accounts"


def test(request):
    return HttpResponse("Hello")


urlpatterns = [path("", test, name="test")]
