import pytest
from django.contrib.auth import get_user_model

from cartdrop.core.models import Brand, ProductCategory, ProductSubcategory
from cartdrop.products.models import (Product, ProductSpecification,
                                      ProductVariation)


@pytest.fixture
def get_new_user():
    def create_new_user(
        number: int,
        email: str,
        username: str,
        password: str,
        is_active: bool = True,
        is_superuser: bool = False,
        is_staff: bool = False,
        is_email_verified: bool = True,
        is_number_verified: bool = True,
        is_disabled: bool = False,
    ):
        user_model = get_user_model()
        return user_model.objects.create_user(
            number=number,
            email=email,
            username=username,
            password=password,
            is_active=is_active,
            is_superuser=is_superuser,
            is_staff=is_staff,
            is_email_verified=is_email_verified,
            is_number_verified=is_number_verified,
            is_disabled=is_disabled,
        )

    return create_new_user


@pytest.fixture
def product_data(get_new_user):
    user = get_new_user(
        number="7208333993",
        email="test@test.com",
        username="testuser",
        password="password123",
    )
    brand = Brand.objects.create(name="test brand")
    category = ProductCategory.objects.create(name="test category")
    subcategory = ProductSubcategory.objects.create(
        name="test subcategory", category=category
    )
    specification = ProductSpecification.objects.create(in_box="test In The box")
    product = Product.objects.create(
        brand=brand,
        name="test product",
        seller=user,
        subcategory=subcategory,
        specification=specification,
    )
    product_variation = ProductVariation.objects.create(
        product=product, price=500, retail_price=450
    )
    return {
        "product__slug": product.slug,
        "uuid": product_variation.uuid,
        "pid": product_variation.pid,
    }
