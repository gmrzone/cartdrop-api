from django import urls
from django.test import TestCase
from django.urls import resolve, reverse
from ..views import *

class ListUrlsTest(TestCase):
    
    def test_category_list(self):
        url = reverse("core:category_list")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, CategoryList)