from crypt import methods

from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .models import Cart

# Create your views here.


class AddToCart(APIView):
    allowed_methods = ["post"]

    def post(self, request):
        uuid = request.data.get("uuid")
        pid = request.data.get("pid")
        cart = Cart(request=request)
        data, status = cart.add(uuid=uuid, pid=pid)
        return Response(data, status=status)


class RemoveFromCart(APIView):
    allowed_methods = ["post"]

    def post(self, request):
        uuid = request.data.get("uuid")
        pid = request.data.get("pid")
        cart = Cart(request=request)
        data, status = cart.remove(uuid=uuid, pid=pid)
        return Response(data, status=status)


class DeleteFromCart(APIView):
    allowed_methods = ["delete"]

    def delete(self, request, uuid, pid):
        # uuid = self.kwargs.get("uuid")
        # pid = self.kwargs.get("pid")
        cart = Cart(request=request)
        data, status = cart.delete(uuid=uuid, pid=pid)
        return Response(data, status=status)


class ApplyCouponCode(APIView):
    allowed_methods = ["post"]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        coupon_code = request.data.get("coupon_code")
        cart = Cart(request=request)
        response = cart.apply_coupon(coupon_code=coupon_code, user=request.user)
        return Response(response)


class GetDetailCart(APIView):
    allowed_methods = ["get"]

    def get(self, request):
        cart = Cart(request=request)
        response = cart.get_cart_detail()
        return Response(response)


class GetBasicCart(APIView):
    allowed_methods = ["get"]

    def get(self, request):
        cart = Cart(request=request)
        return Response(cart.get_basic_cart(), status=HTTP_200_OK)
