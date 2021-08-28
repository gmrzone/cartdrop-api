from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import ProductVariation
from .serializers import ProductVariationSerializer

# Create your views here.


class ProductVariationList(ListAPIView):
    serializer_class = ProductVariationSerializer
    http_method_names = ["get"]

    def get_queryset(self):
        queryset = (
            ProductVariation.objects.filter(active=True)
            .select_related(
                "color",
                "laptop_variant",
                "mobile_variant",
                "tv_variant",
                "ac_capacity_variant",
                "ac_star_variant",
                "book_variation",
                "size",
                "product",
                "product__brand",
                "product__seller",
                "product__subcategory",
            )
            .prefetch_related("images")
        )
        return queryset
