import json

import pytest
from dateutil.relativedelta import relativedelta
from django.urls import reverse
from django.utils import timezone


@pytest.mark.django_db
def test_add_to_cart_view(client, product_data):
    url = reverse("cart:add")
    product_uuid = product_data["uuid"]
    product_pid = product_data["pid"]
    product_key = f"{product_uuid}_{product_pid}"
    #  First test without passing any data for uuid and pid
    response = client.post(url)
    assert response.status_code == 400
    assert response.data["message"] == "Product UUID & PID Cannot be blank"

    # Now try with only uuid
    response = client.post(url, data={"uuid": product_uuid})
    assert response.status_code == 400
    assert response.data["message"] == "Product PID Cannot be blank"

    # Now try with only pid
    response = client.post(url, data={"pid": product_pid})
    assert response.status_code == 400
    assert response.data["message"] == "Product UUID Cannot be blank"

    # Now we add product which is not in the database
    response = client.post(url, data={"uuid": product_uuid, "pid": "WRONG_PID"})
    assert response.status_code == 403
    assert (
        response.data["message"]
        == "The product you are trying to buy is currently not available."
    )

    # Now we add proper product
    response = client.post(url, data={"uuid": product_uuid, "pid": product_pid})
    assert response.status_code == 200
    assert response.data["message"] == "Sucessfully added test product to cart."

    # Now we check if the product is added in cart
    # Now check and assert the cart to match the quantity
    basic_cart_url = reverse("cart:get_cart_basic")
    response = client.get(basic_cart_url)
    assert response.data["products"][product_key]["quantity"] == 1


@pytest.mark.django_db
def test_remove_from_cart(client, product_data):
    # First Get Cart instance with 4 products in cart
    product_uuid = product_data["uuid"]
    product_pid = product_data["pid"]
    product_key = f"{product_uuid}_{product_pid}"
    # First Add few products
    add_url = reverse("cart:add")
    client.post(add_url, data={"uuid": product_uuid, "pid": product_pid})
    client.post(add_url, data={"uuid": product_uuid, "pid": product_pid})
    client.post(add_url, data={"uuid": product_uuid, "pid": product_pid})

    # Now check and assert the cart to match the quantity
    basic_cart_url = reverse("cart:get_cart_basic")
    response = client.get(basic_cart_url)
    assert response.data["products"][product_key]["quantity"] == 3
    # Now we test the remove from cart view
    # First we try to call the endpoint without any uuid and pid
    remove_url = reverse("cart:remove")
    response = client.post(remove_url)
    assert response.status_code == 400
    assert response.data["message"] == "Product UUID & PID Cannot be blank"

    # Now we pass uuid but no pid
    response = client.post(remove_url, data={"uuid": product_uuid})
    assert response.status_code == 400
    assert response.data["message"] == "Product PID Cannot be blank"

    # Now we pass only pid
    response = client.post(remove_url, data={"pid": product_pid})
    assert response.status_code == 400
    assert response.data["message"] == "Product UUID Cannot be blank"

    # Now we pass wrong pid or uuid
    response = client.post(remove_url, data={"uuid": product_uuid, "pid": "WRONG_PID"})
    assert response.status_code == 403
    assert response.data["message"] == "Product is not in your cart."

    # Now we pass the right uuid and pid
    # Now we pass wrong pid or uuid
    response = client.post(remove_url, data={"uuid": product_uuid, "pid": product_pid})
    assert response.status_code == 200
    assert response.data["message"] == "Product quantity decreased by 1"

    ## Now check the basic cart for quantity it should be decremented by 1
    basic_cart_url = reverse("cart:get_cart_basic")
    response = client.get(basic_cart_url)
    assert response.data["products"][product_key]["quantity"] == 2


@pytest.mark.django_db
def test_delete_from_cart(client, product_data):
    product_uuid = product_data["uuid"]
    product_pid = product_data["pid"]
    product_key = f"{product_uuid}_{product_pid}"
    headers = {"Content-type": "application/json", "Accept": "application/json"}
    # First Add few products
    add_url = reverse("cart:add")
    client.post(
        add_url, data={"uuid": product_uuid, "pid": product_pid}, headers=headers
    )
    client.post(
        add_url, data={"uuid": product_uuid, "pid": product_pid}, headers=headers
    )
    client.post(
        add_url, data={"uuid": product_uuid, "pid": product_pid}, headers=headers
    )
    client.post(
        add_url, data={"uuid": product_uuid, "pid": product_pid}, headers=headers
    )

    # Now check and assert the cart to match the quantity
    basic_cart_url = reverse("cart:get_cart_basic")
    response = client.get(basic_cart_url, headers=headers)
    assert response.data["products"][product_key]["quantity"] == 4

    # Now check the delete view
    delete_url = reverse(
        "cart:delete", kwargs={"uuid": product_uuid, "pid": product_pid}
    )
    response = client.delete(delete_url)
    assert response.status_code == 200
    assert response.data["message"] == "Sucessfully removed product from the cart"

    # Now check if the product is completely deleted from cart
    response = client.get(basic_cart_url, headers=headers)
    assert response.data["products"] == {}


@pytest.mark.django_db
def test_apply_coupon_code_view(client, get_coupon):
    apply_coupon_url = reverse("cart:apply_coupon")
    now = timezone.now()
    valid_from = now - relativedelta(days=1)
    valid_to = now + relativedelta(months=1)
    get_coupon(
        code="TEST_COUPON",
        valid_from=valid_from,
        valid_to=valid_to,
        discount=25,
        reusable_type=False,
    )

    # Apply Coupon endpoint is for authenticated user only so we should get error
    # If we hit that endpoint without authentication

    response = client.post(apply_coupon_url, data={"coupon_code": "TEST_COUPON"})
    assert response.status_code == 401
    assert response.data["detail"] == "Authentication credentials were not provided."
