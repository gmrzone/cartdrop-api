import django
from django.conf import settings
from django.db import models

from ..products.models import ProductVariation

# Create your models here.


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def save(self):
        self.session.modified = True

    def add(self, uuid: str, pid: str, quantity: int = 1) -> dict:
        cart_updated = False
        product_key = f"{uuid}_{pid}"
        if product_key in self.cart:
            self.cart[product_key]["quantity"] += 1
            cart_updated = True
            response = {"status": "ok", "message": "Sucessfuly added "}
        else:
            try:
                product_variation = ProductVariation.objects.get(
                    uuid=uuid, pid=pid, active=True
                )
            except:
                response = {
                    "status": "error",
                    "message": "The product you are trying to buy is currently not available.",
                }
            else:
                self.cart[product_key] = {
                    "quantity": quantity,
                    "price": product_variation.price,
                }
                cart_updated = True
                response = {
                    "status": "ok",
                    "message": f"Sucessfully added {product_variation} to cart.",
                }
        if cart_updated:
            self.save()
        return response

    def remove(self, uuid: str, pid: str, quantity: int = 1) -> dict:
        product_key = f"{uuid}_{pid}"
        cart_updated = False
        if product_key in self.cart:
            if self.cart[product_key]["quantity"] > quantity:
                self.cart[product_key]["quantity"] -= quantity
                response = {
                    "status": "ok",
                    "message": f"Product quantity decreased by {quantity}",
                }
            else:
                del self.cart[product_key]
                response = {
                    "status": "ok",
                    "message": "Sucessfully removed product from the cart",
                }
            cart_updated = True
        else:
            response = {"status": "error", "message": "Product not available"}
        if cart_updated:
            self.save()
        return response

    def delete(self, uuid: str, pid: str) -> dict:
        product_key = f"{uuid}_{pid}"
        cart_updated = False
        if product_key in self.cart:
            del self.cart[product_key]
            response = {
                "status": "ok",
                "message": "Sucessfully removed product from the cart",
            }
            cart_updated = True
        else:
            response = {
                "status": "error",
                "message": "Product Not found",
            }
        if cart_updated:
            self.save()
        return response
