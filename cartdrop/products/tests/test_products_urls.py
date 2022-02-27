from django.urls import reverse, resolve
from ..views import *


def test_featured_product_url():
    url = reverse("products:featured")
    resolver = resolve(url)
    assert resolver.func.view_class == FeaturedProductVariationList


def test_top_category_product_variation():
    url = reverse("products:top_category_products", kwargs={"category": "mobiles"})
    resolver = resolve(url)
    assert resolver.func.view_class == TopCategoryProductVariation


def test_product_list_for_category():
    url = reverse("products:category_products", kwargs={"category": "mobiles"})
    resolver = resolve(url)
    assert resolver.func.view_class == ProductListForCategory
    
def test_product_variation_detail():
    url = reverse("products:product_variation_detail", kwargs={"product__slug": "apple-iphone-se", "uuid": "54b5423d-f00a-43c1-a605-584c932b9f92", "pid": "MBLOGTKIADMSGKIKZJ"})
    resolver = resolve(url)
    assert resolver.func.view_class == ProductVariationDetail
