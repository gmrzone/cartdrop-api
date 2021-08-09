from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
# Create your views here.


class GetCurrentUser(APIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)

        return Response(data=serializer.data, status=HTTP_200_OK)
    