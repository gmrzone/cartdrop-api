from django.urls import path

from .views import ProductVariationList, TopCategoryProductVariationList

app_name = "products"


urlpatterns = [
    path("featured/", ProductVariationList.as_view(), name="featured"),
    path(
        "<str:category>/top/",
        TopCategoryProductVariationList.as_view(),
        name="top_category_products",
    ),
]
