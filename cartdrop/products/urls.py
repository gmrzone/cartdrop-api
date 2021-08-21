from django.http.response import HttpResponse
from django.urls import path

app_name = "products"


def test(request):
    return HttpResponse("Working")


urlpatterns = [path("test/", test, name="test_new")]
