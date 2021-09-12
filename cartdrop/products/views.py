from django.db.models import F, query
from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import ProductVariation
from .serializers import ProductVariationBaseSerializer

# Create your views here.


class ProductVariationList(ListAPIView):
    serializer_class = ProductVariationBaseSerializer
    http_method_names = ["get"]

    def get_queryset(self):
        # queryset to return a unique product variants that has discount percent greater then 20%. This is temperary we will add a better algorithm for featured products
        queryset = (
            ProductVariation.objects.annotate(
                discount_percent=(100 - (F("price") * 100 / F("retail_price")))
            )
            .filter(active=True, discount_percent__gt=10)
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
            .distinct("product__id")
        )

        return queryset
