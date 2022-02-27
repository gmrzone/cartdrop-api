from django.db.models import F
from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     get_object_or_404)

from .models import ProductVariation
from .pagination import ProductVariationPagination
from .serializers import ProductVariationBaseSerializer

# Create your views here.


class FeaturedProductVariationList(ListAPIView):
    serializer_class = ProductVariationBaseSerializer
    http_method_names = ["get"]

    def get_queryset(self):
        # TODO:  queryset to return a unique product variants that has discount percent greater then 20%. This is temperary we will add a better algorithm for featured products
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
            .order_by()
            .distinct("product__id")
        )

        return queryset


# View to return top products based on passed category slug
class TopCategoryProductVariation(ListAPIView):
    serializer_class = ProductVariationBaseSerializer
    http_method_names = ["get"]

    def get_queryset(self):
        category = self.kwargs["category"]
        # TODO:  FIlter product variation by category and order by overall rating desc so that top rated product are first
        # WIll change it later so the this queryset will order productVariation by no of purchases using redis
        queryset = (
            ProductVariation.objects.filter(
                product__subcategory__category__slug=category
            )
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
            .order_by("-product__overall_rating")
        )

        return queryset


# TODO : View to get products based on categories (Will add filters later)
class ProductListForCategory(ListAPIView):

    serializer_class = ProductVariationBaseSerializer
    http_method_names = ["get"]
    pagination_class = ProductVariationPagination
    pagination_class.page_size = 6

    def get_queryset(self):
        category = self.kwargs["category"]
        queryset = (
            ProductVariation.objects.filter(
                product__subcategory__category__slug=category
            )
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


# class ProductBrandsByCategory(ListAPIView):
#     serializer_class = ProductBrandSerializer
#     http_method_names = ["get"]

#     def get_queryset(self):
#         category = self.kwargs["category"]
#         queryset = Product.objects.filter(
#             subcategory__category__slug=category
#         ).select_related("brand").distinct("brand")
#         return queryset


class ProductVariationDetail(RetrieveAPIView):
    serializer_class = ProductVariationBaseSerializer
    http_method_names = ["get"]
    lookup_fields = ("uuid", "pid", "product__slug")

    def get_queryset(self):
        queryset = (
            ProductVariation.objects.all()
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

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filters = {
            field: self.kwargs[field]
            for field in self.lookup_fields
            if self.kwargs.get(field, None)
        }
        obj = get_object_or_404(queryset=queryset, **filters)
        self.check_object_permissions(self.request, obj)
        return obj
