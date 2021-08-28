from django.http.response import HttpResponse
from django.urls import path
from .views import ProductVariationList
app_name = "products"





urlpatterns = [
    path('featured/', ProductVariationList.as_view(), name="featured")
]
