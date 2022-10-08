from rest_framework.generics import ListAPIView

from .models import Brand, ProductCategory, ProductSubcategory
from .serializers import (BrandSerializer, ProductCategorySerializer,
                          ProductSubcategorySerializer)
from .pagination import DefaultPageNoPagination


class CategoryList(ListAPIView):
    serializer_class = ProductCategorySerializer
    http_method_names = ["get"]
    pagination_class = DefaultPageNoPagination

    def get_queryset(self):
        queryset = ProductCategory.objects.all().prefetch_related("category_images")
        return queryset


class SubcategoryList(ListAPIView):
    serializer_class = ProductSubcategorySerializer
    pagination_class = DefaultPageNoPagination

    def get_queryset(self):
        category = self.kwargs["category"]
        queryset = ProductSubcategory.objects.filter(
            category__slug=category
        ).prefetch_related("subcategory_images", "coupons")
        return queryset


class SubcategoryOfferList(ListAPIView):
    serializer_class = ProductSubcategorySerializer
    http_method_names = ["get"]

    def get_queryset(self):
        queryset = ProductSubcategory.objects.all().exclude(coupons=None)
        return queryset


class ProductBrandsByCategory(ListAPIView):
    serializer_class = BrandSerializer
    http_method_names = ["get"]

    def get_queryset(self):
        category = self.kwargs["category"]
        queryset = Brand.objects.filter(
            product_list__subcategory__category__slug=category
        ).distinct()
        return queryset
