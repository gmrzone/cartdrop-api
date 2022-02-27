
import pytest
from cartdrop.products.models import Product, ProductVariation, ProductSpecification
from cartdrop.core.models import Brand, ProductCategory, ProductSubcategory
from django.contrib.auth import get_user_model


@pytest.fixture
def product_data(db):
    user_model = get_user_model()
    user = user_model.objects.create_user(number="7208333993", email="test@test.com", username="testuser", password="password123", is_active=True)
    brand = Brand.objects.create(name="test brand")
    category = ProductCategory.objects.create(name="test category")
    subcategory = ProductSubcategory.objects.create(name="test subcategory", category=category)
    specification = ProductSpecification.objects.create(in_box="test In The box")
    product = Product.objects.create(brand=brand, name="test product", seller=user, subcategory=subcategory, specification=specification)
    product_variation = ProductVariation.objects.create(product=product, price=500, retail_price=450)
    return {"product__slug": product.slug, "uuid": product_variation.uuid, "pid": product_variation.pid}

