from django.urls import path

from .views import (AddToCart, ApplyCouponCode, DeleteFromCart, GetBasicCart,
                    GetDetailCart, RemoveFromCart)

app_name = "cart"

urlpatterns = [
    path("add/", AddToCart.as_view(), name="add"),
    path("remove/", RemoveFromCart.as_view(), name="remove"),
    path("delete/<uuid:uuid>/<str:pid>/", DeleteFromCart.as_view(), name="delete"),
    path("get-cart/detail/", GetDetailCart.as_view(), name="get_cart_detail"),
    path("get-cart/basic/", GetBasicCart.as_view(), name="get_cart_basic"),
    path("apply/coupon/", ApplyCouponCode.as_view(), name="apply_coupon"),
]
