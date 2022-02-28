from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from .models import CartDropUser

# Create your views here.


class GetCurrentUser(APIView):
    http_method_names = ["get"]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)

        return Response(data=serializer.data, status=HTTP_200_OK)


class Signup(CreateAPIView):
    http_method_names = ["post"]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        username = request.data.get("username").lower()
        response = Response()
        try:
            user = CartDropUser.objects.get(username=username)
            if user.is_disabled or not user.is_active:
                response.data = {
                    "status": "error",
                    "message": "Your account has been disabled or inactive. Please contact us to get more detail"
                }
                response.status_code = HTTP_403_FORBIDDEN
            else:
                response.data = {
                    "status": "ok",
                    "message": f"You already have a account with us. Please login using username {user.username}"
                }
                response.status_code = HTTP_200_OK
        except CartDropUser.DoesNotExist:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                self.perform_create(serializer)
                response.data = {
                    "status": "ok",
                    "message": "Your Account has been successfully created. An email with verification link has been sent to your email. Please use that link to verify your account."
                }
                response.status_code = HTTP_200_OK
            else:
                response.data = {
                "status": "error",
                "message": serializer.errors
                }
                response.status_code = HTTP_403_FORBIDDEN
        finally:
            return response
