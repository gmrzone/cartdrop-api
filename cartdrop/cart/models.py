from datetime import timedelta

from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.core.exceptions import MultipleObjectsReturned
from django.utils import timezone
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,
                                   HTTP_403_FORBIDDEN)

from ..core.models import CouponCode
from ..products.models import ProductVariation
from ..products.serializers import ProductVariationDetailSerializer

# Create your models here.

#  TODO: This Cart class has not been tested Please test it before implementing it
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {
                "products": {},
                "cart_detail": {},
            }

        self.cart = cart

    def save(self):
        self.session.modified = True

    def add(self, uuid: str, pid: str, quantity: int = 1) -> dict:
        if not uuid or not pid:
            message = "Product "
            message += (
                "UUID & PID "
                if not uuid and not pid
                else "PID "
                if not pid
                else "UUID "
            )
            message += "Cannot be blank"
            data, status = {"status": "error", "message": message}, HTTP_400_BAD_REQUEST
            return data, status
        cart_updated = False
        product_key = f"{uuid}_{pid}"
        if product_key in self.cart["products"]:
            self.cart["products"][product_key]["quantity"] += 1
            cart_updated = True
            data, status = {"status": "ok", "message": "Sucessfuly added "}, HTTP_200_OK
        else:
            try:
                product_variation = ProductVariation.objects.get(
                    uuid=uuid, pid=pid, active=True
                )
            except ProductVariation.DoesNotExist:
                data, status = {
                    "status": "error",
                    "message": "The product you are trying to buy is currently not available.",
                }, HTTP_403_FORBIDDEN
            else:
                self.cart["products"][product_key] = {
                    "quantity": quantity,
                    "price": str(product_variation.price),
                }
                cart_updated = True
                data, status = {
                    "status": "ok",
                    "message": f"Sucessfully added {product_variation} to cart.",
                }, HTTP_200_OK
        if cart_updated:
            self.save()
        return data, status

    def remove(self, uuid: str, pid: str, quantity: int = 1) -> dict:
        if not uuid or not pid:
            message = "Product "
            message += (
                "UUID & PID "
                if not uuid and not pid
                else "PID "
                if not pid
                else "UUID "
            )
            message += "Cannot be blank"
            data, status = {"status": "error", "message": message}, HTTP_400_BAD_REQUEST
            return data, status
        product_key = f"{uuid}_{pid}"
        cart_updated = False
        if product_key in self.cart["products"]:
            if self.cart["products"][product_key]["quantity"] > quantity:
                self.cart["products"][product_key]["quantity"] -= quantity
                data, status = {
                    "status": "ok",
                    "message": f"Product quantity decreased by {quantity}",
                }, HTTP_200_OK
            else:
                self.delete(uuid, pid)
            cart_updated = True
        else:
            data, status = {
                "status": "error",
                "message": "Product is not in your cart.",
            }, HTTP_403_FORBIDDEN
        if cart_updated:
            self.save()
        return data, status

    def delete(self, uuid: str, pid: str) -> dict:
        if not uuid or not pid:
            message = "Product "
            message += (
                "UUID & PID "
                if not uuid and not pid
                else "PID "
                if not pid
                else "UUID "
            )
            message += "Cannot be blank"
            data, status = {"status": "error", "message": message}, HTTP_400_BAD_REQUEST
            return data, status
        product_key = f"{uuid}_{pid}"
        cart_updated = False
        if product_key in self.cart["products"]:
            del self.cart["products"][product_key]
            data, status = {
                "status": "ok",
                "message": "Sucessfully removed product from the cart",
            }, HTTP_200_OK
            cart_updated = True
        else:
            data, status = {
                "status": "error",
                "message": "Product Not found.",
            }, HTTP_400_BAD_REQUEST
        if cart_updated:
            self.save()
        return data, status

    def apply_coupon_to_session(self, coupon):
        self.cart["cart_detail"]["coupon"] = coupon.code
        self.cart["cart_detail"]["discount"] = coupon.discount
        response = {
            "status": "ok",
            "message": f"sucessfully applied coupon {coupon.code} with discount {coupon.discount}%",
        }
        self.save()
        return response

    @staticmethod
    def get_remaning_time(current_time, target_time):
        remaning_datetime = target_time - current_time
        days = remaning_datetime.days
        # parsed_remaning_time = ""
        # if remaning_datetime.year:
        #     parsed_remaning_time += f"{remaning_datetime.year} year{'s' if remaning_datetime.year > 1 else ''}, "
        # if remaning_datetime.month:
        #     parsed_remaning_time += f"{remaning_datetime.month} month{'s' if remaning_datetime.month > 1 else ''}, "
        # if remaning_datetime.day:
        #     parsed_remaning_time += f"{remaning_datetime.day} day{'s' if remaning_datetime.day > 1 else ''}, "
        # if remaning_datetime.hour:
        #     parsed_remaning_time += f"{remaning_datetime.hour} day{'s' if remaning_datetime.hour > 1 else ''}, "
        # if remaning_datetime.minute:
        #     parsed_remaning_time += f"{remaning_datetime.minute} day{'s' if remaning_datetime.minute > 1 else ''}, "
        # if remaning_datetime.second:
        #     parsed_remaning_time += f"{remaning_datetime.second} day{'s' if remaning_datetime.second > 1 else ''}, "
        # return parsed_remaning_time
        return f"{days} Day{'s' if days > 1 else ''}"

    def apply_reusable_coupon(self, coupon, user_coupons, date_now):
        if user_coupons.reusable_type == CouponCode.CouponReusableTypeChoises.MONTHLY:
            if user_coupons.created <= (date_now - relativedelta(months=1)):
                response = self.apply_coupon_to_session(coupon)
            else:
                coupon_next_available_date = user_coupons.created + relativedelta(
                    months=1
                )
                remaning_time = Cart.get_remaning_time(
                    date_now, coupon_next_available_date
                )
                response = {
                    "status": "error",
                    "message": f"This have already used this coupon on {user_coupons.created.strftime('%d %B, %Y')}. Please try again after {remaning_time}",
                }
        elif user_coupons.reusable_type == CouponCode.CouponReusableTypeChoises.YEARLY:

            if user_coupons.created <= (date_now - relativedelta(years=1)):
                response = self.apply_coupon_to_session(coupon)
            else:
                coupon_next_available_date = user_coupons.created + relativedelta(
                    years=1
                )
                remaning_time = Cart.get_remaning_time(
                    date_now, coupon_next_available_date
                )
                response = {
                    "status": "error",
                    "message": f"This have already used this coupon on {user_coupons.created.strftime('%d %B, %Y')}. Please try again after {remaning_time}",
                }
        return response

    # Note: User can only apply coupon when he is authenticated so we can check if the user has already
    # Applied a coupon or not
    def apply_coupon(self, coupon_code, user):
        if not coupon_code:
            return {"status": "error", "message": "Coupon code cannot be blank."}
        date_now = timezone.now()
        try:
            # Check if the coupon exist and is active
            coupon = CouponCode.objects.get(
                code__iexact=coupon_code,
                active=True,
                valid_from__lte=date_now,
                valid_to__gte=date_now,
            )
        except CouponCode.DoesNotExist:
            response = {
                "status": "error",
                "message": f"The Coupon code {coupon_code} is not valid or has been expired.",
            }
        except MultipleObjectsReturned:
            response = {
                "status": "error",
                "message": "This Coupon code is currently not availabe. Please try again later",
            }
        else:
            # If the user has already applied this coupon
            user_coupon = user.coupon_codes.filter(code__iexact=coupon_code).first()
            if user_coupon:
                # If coupon is only for single use then return error response
                if (
                    user_coupon.reusable_type
                    == CouponCode.CouponReusableTypeChoises.SINGLE
                ):
                    response = {
                        "status": "error",
                        "message": f"Sorry you have already used this coupon on {user_coupon.created.strftime('%d %B, %Y')}",
                    }
                else:
                    response = self.apply_reusable_coupon(coupon, user_coupon, date_now)
            else:
                # If there is no product in the cart then we cannot apply coupon
                if self.cart["products"] == {}:
                    response = {
                        "status": "error",
                        "message": "Cannot apply coupon on empty cart.",
                    }
                # If the user has not applied this coupon then go ahead and save it in session and when
                # The user finishes the order then create relation between that user and coupon so that
                # Next time we can find if the user has applied this coupon
                else:
                    response = self.apply_coupon_to_session(coupon)
        return response

    def __iter__(self):
        for key in self.cart["products"].keys():
            yield key

    # TODO: Need to improve this method whenever we can test this
    def get_cart_detail(self):
        cart = self.cart["products"].copy()
        cart_detail = self.cart["cart_detail"].copy()

        uuids = []
        pids = []
        for key in self:
            uuid, pid = key.split("_")
            uuids.append(uuid)
            pids.append(pid)

        product_variations = ProductVariation.objects.filter(
            uuid__in=uuids, pid__in=pids
        )
        cart_detail["total_without_discount"] = 0
        for product in product_variations:
            product_key = f"{product.uuid}_{product.pid}"
            cart[product_key]["product"] = ProductVariationDetailSerializer(
                product, many=False
            ).data
            cart[product_key]["total"] = product.price * cart[product_key]["quantity"]
            cart_detail["total_without_discount"] += (
                product.price * cart[product_key]["quantity"]
            )

        cart_detail["discount_amount"] = (
            cart_detail["total_without_discount"] * cart_detail["discount"] / 100
        )
        cart_detail["final_total"] = (
            cart_detail["total_without_discount"] - cart_detail["discount_amount"]
        )
        return {"cart": cart, "cart_detail": cart_detail}

    def get_basic_cart(self):
        return self.cart
