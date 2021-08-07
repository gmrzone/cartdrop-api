from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import ProductCategorySerializer
from .models import ProductCategory
# Create your views here.


class CategoryList(ListAPIView):
    serializer_class = ProductCategorySerializer

    def get_queryset(self):
        queryset = ProductCategory.objects.all().prefetch_related('category_images')
        return queryset



