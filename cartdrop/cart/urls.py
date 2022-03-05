from django.urls import path
from .views import test_cart_view


app_name = "cart"

urlpatterns = [path("test/", test_cart_view, name="test-cart")]
