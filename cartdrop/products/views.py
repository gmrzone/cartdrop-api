from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import ProductVariationSerializer
from .models import ProductVariation
# Create your views here.


class ProductVariationList(ListAPIView):
    serializer_class = ProductVariationSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = ProductVariation.objects.filter(active=True)
        return queryset

