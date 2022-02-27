from django.urls import resolve, reverse

from ..views import *


def test_category_list_url():
    url = reverse("core:category_list")
    resolver = resolve(url)
    assert resolver.func.view_class == CategoryList


def test_subcategory_list_url():
    url = reverse("core:subcategory_list", kwargs={"category": "mobiles"})
    resolver = resolve(url)
    assert resolver.func.view_class == SubcategoryList


def test_offers_list_url():
    url = reverse("core:subcategory_offers")
    resolver = resolve(url)
    assert resolver.func.view_class == SubcategoryOfferList


def test_brand_by_category_url():
    url = reverse("core:brand_by_category_new", kwargs={"category": "mobiles"})
    resolver = resolve(url)
    assert resolver.func.view_class == ProductBrandsByCategory
