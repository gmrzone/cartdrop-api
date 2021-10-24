from django.test import TestCase
from django.urls import resolve, reverse

from ..views import *
from ...products.views import *


class ListUrlsTest(TestCase):
    def test_category_list(self):
        url = reverse("core:category_list")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, CategoryList)

    def test_subcategory_list(self):
        url = reverse("core:subcategory_list", kwargs={"category": "appliances"})
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, SubcategoryList)

    def test_featured_products(self):
        url = reverse("products:featured")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, ProductVariationList)

    def test_top_products_based_on_category(self):
        url = reverse(
            "products:top_category_products", kwargs={"category": "appliances"}
        )
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, TopCategoryProductVariationList)
