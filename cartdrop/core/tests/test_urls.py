from django.test import TestCase
from django.urls import resolve, reverse

from ...products.views import *
from ..views import *


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
        self.assertEqual(resolver.func.view_class, FeaturedProductVariationList)

    def test_top_products_based_by_category(self):
        url = reverse(
            "products:top_category_products", kwargs={"category": "appliances"}
        )
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, TopCategoryProductVariation)

    def test_products_based_by_category(self):
        url = reverse("products:category_products", kwargs={"category": "appliances"})
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, ProductListForCategory)

    # def test_product_brands_by_category(self):
    #     url = reverse("products:brands_by_category", kwargs={"category": "appliances"})
    #     resolver = resolve(url)
    #     self.assertEqual(resolver.func.view_class, ProductBrandsByCategory)

    def test_product_brands_by_category(self):
        url = reverse("core:brand_by_category_new", kwargs={"category": "appliances"})
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, ProductBrandsByCategory)

    def test_product_variation_detail(self):
        url = reverse("products:product_variation_detail", kwargs={"uuid": "69792a43-c471-48c1-a247-c7a9ee193531", "pid": "MBLTPZJQAFHUVMGCLS", "product__slug": "samsung-galaxy-s20-fe-5g"})
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, ProductVariationDetail)
