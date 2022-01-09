from django.urls import path

from .views import (FeaturedProductVariationList, ProductListForCategory,
                    ProductVariationDetail, TopCategoryProductVariation)

app_name = "products"


urlpatterns = [
    path("featured/", FeaturedProductVariationList.as_view(), name="featured"),
    path(
        "<str:category>/top/",
        TopCategoryProductVariation.as_view(),
        name="top_category_products",
    ),
    path("<str:category>/", ProductListForCategory.as_view(), name="category_products"),
    path(
        "<slug:product__slug>/<str:uuid>/<str:pid>/",
        ProductVariationDetail.as_view(),
        name="product_variation_detail",
    ),
]
