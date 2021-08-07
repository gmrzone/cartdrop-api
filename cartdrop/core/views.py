from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from .serializers import ProductCategorySerializer
from .models import ProductCategory


class CategoryList(ListAPIView):
    serializer_class = ProductCategorySerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = ProductCategory.objects.all().prefetch_related('category_images')
        return queryset



