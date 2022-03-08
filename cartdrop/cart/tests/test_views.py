import json

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_add_to_cart_view(client, product_data):
    url = reverse("cart:add")
    product_uuid = product_data["uuid"]
    product_pid = product_data["pid"]

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

    print(response.data)
