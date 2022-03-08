from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cart

# Create your views here.


class AddToCart(APIView):
    allowed_methods = ["post"]

    def post(self, request):
        uuid = request.data.get("uuid")
        pid = request.data.get("pid")
        cart = Cart(request=request)
        response = cart.add(uuid=uuid, pid=pid)
        return Response(response)


class RemoveFromCart(APIView):
    allowed_methods = ["post"]

    def post(self, request):
        uuid = request.data.get("uuid")
        pid = request.data.get("pid")
        cart = Cart(request=request)
        response = cart.remove(uuid=uuid, pid=pid)
        return Response(response)


class DeleteFromCart(APIView):
    allowed_methods = ["delete"]

    def delete(self, request):
        uuid = request.data.get("uuid")
        pid = request.data.get("pid")
        cart = Cart(request=request)
        response = cart.delete(uuid=uuid, pid=pid)
        return Response(response)


class ApplyCouponCode(APIView):
    allowed_methods = ["post"]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        coupon_code = request.data.get("coupon_code")
        cart = Cart(request=request)
        response = cart.apply_coupon(coupon_code=coupon_code, user=request.user)
        return Response(response)


class GetCart(APIView):
    allowed_methods = ["post"]

    def get(self, request):
        cart = Cart(request=request)
        response = cart.get_cart_detail()
        return Response(response)
