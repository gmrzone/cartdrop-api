from django.urls import resolve, reverse

from ..views import *


def test_add_to_cart_url():
    url = reverse("cart:add")
    resolver = resolve(url)
    assert resolver.func.view_class == AddToCart


def test_remove_from_cart_url():
    url = reverse("cart:remove")
    resolver = resolve(url)
    assert resolver.func.view_class == RemoveFromCart


def test_delete_from_cart_url():
    url = reverse("cart:delete")
    resolver = resolve(url)
    assert resolver.func.view_class == DeleteFromCart


def test_get_cart_detail_url():
    url = reverse("cart:get_cart_detail")
    resolver = resolve(url)
    assert resolver.func.view_class == GetDetailCart


def test_get_cart_basic_url():
    url = reverse("cart:get_cart_basic")
    resolver = resolve(url)
    assert resolver.func.view_class == GetBasicCart


def test_apply_coupon_url():
    url = reverse("cart:apply_coupon")
    resolver = resolve(url)
    assert resolver.func.view_class == ApplyCouponCode
