from django.urls import path
from .views import (
    FeaturedProductVariationList,
    TopCategoryProductVariation,
    ProductListForCategory,
)

app_name = "products"


urlpatterns = [
    path("featured/", FeaturedProductVariationList.as_view(), name="featured"),
    path(
        "<str:category>/top/",
        TopCategoryProductVariation.as_view(),
        name="top_category_products",
    ),
    path("<str:category>/", ProductListForCategory.as_view(), name="category_products"),
]
