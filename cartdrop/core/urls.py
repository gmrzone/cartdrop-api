from django.urls import path

from .views import CategoryList, SubcategoryOfferList, SubcategoryList

app_name = "core"


urlpatterns = [
    path("categories/", CategoryList.as_view(), name="category_list"),
    path(
        "subcategory/<str:category>/",
        SubcategoryList.as_view(),
        name="subcategory_list",
    ),
    path(
        "offers/", SubcategoryOfferList.as_view(), name="subcategory_offers"
    ),
]
