import pytest
from django.contrib.auth import get_user_model
from django.http import HttpRequest

from cartdrop.cart.models import Cart
from cartdrop.core.models import (Brand, CouponCode, ProductCategory,
                                  ProductSubcategory)
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


@pytest.fixture
def get_coupon():
    def wrapper(code, discount, valid_from, valid_to, reusable_type, subcategory=None):
        coupon = CouponCode.objects.create(
            code=code,
            discount=discount,
            valid_from=valid_from,
            valid_to=valid_to,
            reusable_type=reusable_type,
            active=True,
        )
        coupon.subcategory.add(subcategory)
        return coupon

    return wrapper


@pytest.fixture
def get_session():
    class Session(dict):
        modified = False

    return Session


@pytest.fixture
def get_request(get_new_user, get_session):
    user = get_new_user(
        number="9220976696",
        email="requesttest@test.com",
        username="testrequestuser",
        password="password123",
    )
    session = get_session()

    def wrapper():
        request = HttpRequest()
        request.user = user
        request.session = session
        return request

    return wrapper


# @pytest.fixture
# def get_cart_with_items(product_data, get_request):
#     def wrapper(cart_item_count, return_product_detail=False):
#         request = get_request()
#         cart = Cart(request=request)
#         product_uuid = product_data["uuid"]
#         product_pid = product_data["pid"]
#         for i in range(cart_item_count):
#             cart.add(uuid=product_uuid, pid=product_pid)

#         return cart, product_data if return_product_detail else cart

#     return wrapper
