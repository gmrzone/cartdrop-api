from rest_framework.generics import ListAPIView

from .models import ProductCategory, ProductSubcategory
from .serializers import ProductCategorySerializer, ProductSubcategorySerializer


class CategoryList(ListAPIView):
    serializer_class = ProductCategorySerializer
    http_method_names = ["get"]

    def get_queryset(self):
        queryset = ProductCategory.objects.all().prefetch_related("category_images")
        return queryset


class SubcategoryList(ListAPIView):
    serializer_class = ProductSubcategorySerializer

    def get_queryset(self):
        category = self.kwargs["category"]
        queryset = ProductSubcategory.objects.filter(
            category__slug=category
        ).prefetch_related("subcategory_images", "coupons")
        return queryset

class categoryProducts(ListAPIView):
    pass



class SubcategoryOfferList(ListAPIView):
    serializer_class = ProductSubcategorySerializer
    http_method_names = ["get"]

    def get_queryset(self):
        queryset = ProductSubcategory.objects.all().exclude(coupons=None)
        return queryset
