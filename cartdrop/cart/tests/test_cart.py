from urllib import request

import pytest
from django.contrib.auth import get_user_model
from django.http import HttpRequest

from ..models import Cart


# Fake Session
class Session(dict):
    modified = False


@pytest.mark.django_db
def test_cart(client, product_data):
    # Get user model and attach user and session to request object
    user_model = get_user_model()
    user = user_model.objects.get(username="testuser")
    request = HttpRequest()
    request.user = user
    session = Session()
    request.session = session
    cart = Cart(request)
    print(cart.session)

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

    # Noe remove a product that does not exist in the cart should return error
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
