from django.urls import path

from .views import (AddToCart, ApplyCouponCode, DeleteFromCart, GetCart,
                    RemoveFromCart)

app_name = "cart"

urlpatterns = [
    path("add/", AddToCart.as_view(), name="add"),
    path("remove/", RemoveFromCart.as_view(), name="remove"),
    path("delete/", DeleteFromCart.as_view(), name="delete"),
    path("get-cart/", GetCart.as_view(), name="get_cart"),
    path("apply/coupon/", ApplyCouponCode.as_view(), name="apply_coupon"),
]
