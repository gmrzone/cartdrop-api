from django.urls import path

from .views import FeaturedProductVariationList, TopCategoryProductVariationList, ProductListForCategory

app_name = "products"


urlpatterns = [
    path("featured/", FeaturedProductVariationList.as_view(), name="featured"),
    path(
        "<str:category>/top/",
        TopCategoryProductVariationList.as_view(),
        name="top_category_products",
    ),
    path("<str:category>/", ProductListForCategory.as_view(), name="category_products")
]
