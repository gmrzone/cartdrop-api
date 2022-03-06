from urllib import request

import pytest
from dateutil.relativedelta import relativedelta
from django.utils import timezone

from ...core.models import CouponCode, UserCouponIntermidiary
from ..models import Cart


# Fake Session
class Session(dict):
    modified = False


@pytest.mark.django_db
def test_cart(product_data, get_request):
    request = get_request()
    cart = Cart(request)
    #  Add Product to cart
    ## First Add wrong product that is not in the db to assert its response
    response = cart.add(uuid="8dce590d-a02a-4d19-92f2-55fa94b8468c", pid="wrong-pid")
    assert response["status"] == "error"
    assert (
        response["message"]
        == "The product you are trying to buy is currently not available."
    )

    # Now we add correct product that was created inside fixure and product
    ## Should be added to cart
    product_uuid = product_data["uuid"]
    product_pid = product_data["pid"]
    product_key = f"{product_uuid}_{product_pid}"
    response = cart.add(uuid=product_uuid, pid=product_pid)
    #  Check Status
    assert response["status"] == "ok"
    # Check if the product has been added to session with quantity and price

    assert cart.cart["products"][product_key]["quantity"] == 1

    # Now add same product and quantity should be incremented by 1
    response = cart.add(uuid=product_uuid, pid=product_pid)
    assert response["status"] == "ok"
    assert cart.cart["products"][product_key]["quantity"] == 2

    # Now remove a product that does not exist in the cart should return error
    response = cart.remove(uuid="8dce590d-a02a-4d19-92f2-55fa94b8468c", pid="wrong-pid")
    assert response["status"] == "error"
    assert response["message"] == "Product is not in your cart."

    # Now remove the same product and quantity should be decremented by 1
    response = cart.remove(uuid=product_uuid, pid=product_pid)
    assert response["status"] == "ok"
    assert cart.cart["products"][product_key]["quantity"] == 1

    # Now test the delete method with wrong product should return error
    response = cart.delete(uuid="8dce590d-a02a-4d19-92f2-55fa94b8468c", pid="wrong-pid")
    assert response["status"] == "error"
    assert response["message"] == "Product Not found."

    # Now test the delete method with correct product and the should be deleted
    response = cart.delete(uuid=product_uuid, pid=product_pid)
    assert response["status"] == "ok"
    assert cart.cart["products"] == {}


@pytest.mark.django_db
def test_apply_coupon(product_data, get_request, get_coupon):

    request = get_request()
    cart = Cart(request)
    valid_from = timezone.now() - relativedelta(days=1)
    valid_to = timezone.now() + relativedelta(days=2)
    coupon = get_coupon(
        "TEST_COUPON",
        50,
        valid_from,
        valid_to,
        CouponCode.CouponReusableTypeChoises.SINGLE,
    )

    # First Apply coupon without adding product to session
    # It should return error

    response = cart.apply_coupon("TEST_COUPON")
    assert response["status"] == "error"
    assert response["message"] == "Cannot apply coupon on empty cart."

    # Now we add product to cart to quantity = 3
    product_uuid = product_data["uuid"]
    product_pid = product_data["pid"]
    product_key = f"{product_uuid}_{product_pid}"
    cart.add(uuid=product_uuid, pid=product_pid)
    cart.add(uuid=product_uuid, pid=product_pid)
    cart.add(uuid=product_uuid, pid=product_pid)

    # Quantity should be 3
    assert cart.cart["products"][product_key]["quantity"] == 3

    # Now we apply wrong coupon
    response = cart.apply_coupon("WRONG_COUPON")
    assert response["status"] == "error"
    assert (
        response["message"]
        == "The Coupon code WRONG_COUPON is not valid or has been expired."
    )

    # Now we apply the right coupon and it should apply and save it in session
    response = cart.apply_coupon("TEST_COUPON")
    assert response["status"] == "ok"
    assert (
        response["message"]
        == "sucessfully applied coupon TEST_COUPON with discount 50%"
    )

    # Now we create a relationship bitween user and coupon so we know that the user has used
    # this coupon atleast once (using custom intermidiary).
    UserCouponIntermidiary.objects.create(user=request.user, coupon=coupon)
    # Now we try to apply the same coupon and it should return error because it was not
    # a Reusable coupon code
    response = cart.apply_coupon("TEST_COUPON")
    assert response["status"] == "error"
