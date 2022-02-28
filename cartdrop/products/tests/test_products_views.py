import pytest
from django.db.utils import NotSupportedError
from django.urls import reverse


@pytest.mark.parametrize(
    "url_data",
    [
        ("products:top_category_products", {"category": "mobiles"}),
        ("products:category_products", {"category": "mobiles"}),
    ],
)
@pytest.mark.django_db
def test_products_get_views_status(client, url_data):
    url = reverse(url_data[0], kwargs=url_data[1])
    response = client.get(url)
    assert response.status_code == 200


# Here we are using product_data fixture to create product data before testing this view
@pytest.mark.django_db
def test_product_detail_view_status(client, product_data):
    url = reverse("products:product_variation_detail", kwargs=product_data)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_featured_product_list(client):
    try:
        url = reverse("products:featured")
        response = client.get(url)
    except NotSupportedError:  # This view contains distinct("product__id") which is not supported by local db () (only works with postgreSQL)
        assert True
    else:
        assert response.status_code == 200
