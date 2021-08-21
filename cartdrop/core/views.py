from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from .models import ProductCategory
from .serializers import ProductCategorySerializer


class CategoryList(ListAPIView):
    serializer_class = ProductCategorySerializer
    http_method_names = ["get"]

    def get_queryset(self):
        queryset = ProductCategory.objects.all().prefetch_related("category_images")
        return queryset
