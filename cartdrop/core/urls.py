from django.http.response import HttpResponse
from django.urls import path

app_name = "core"


def test(request):
    return HttpResponse("core App")


urlpatterns = [path("test/", test, name="test2")]
