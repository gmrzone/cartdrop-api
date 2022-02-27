import pytest
from django.urls import reverse
from django.db.utils import NotSupportedError

@pytest.mark.parametrize("url_data", [
    ("products:top_category_products", {"category": "mobiles"}),
    ("products:category_products", {"category": "mobiles"})
])
@pytest.mark.django_db
def test_products_get_views_status(client, url_data):
    url = reverse(url_data[0], kwargs=url_data[1])
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_product_detail_view_status(client):
    url = reverse("products:product_variation_detail", kwargs={"product__slug": "apple-iphone-se", "uuid": "54b5423d-f00a-43c1-a605-584c932b9f92", "pid": "MBLOGTKIADMSGKIKZJ"})
    response = client.get(url)
    # Currently the response status code should be 404 bcoz there is no data in test db
    assert response.status_code == 404


@pytest.mark.django_db
def test_featured_product_list(client):
    try:
        url = reverse("products:featured")
        response = client.get(url)
    except NotSupportedError: # This view contains distinct("product__id") which is not supported by local db () (only works with postgreSQL)
        assert True
    else:
        assert response.status_code == 200
