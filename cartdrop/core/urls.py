from django.http.response import HttpResponse
from django.urls import path
from .views import *

app_name = "core"





urlpatterns = [
    path("categories/", CategoryList.as_view(), name="category_list")
    ]
