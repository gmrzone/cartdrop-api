import pytest
from django.urls import reverse


@pytest.mark.parametrize(
    "url_data",
    [
        ("core:category_list", {}),
        ("core:subcategory_list", {"category": "mobiles"}),
        ("core:subcategory_offers", {}),
        ("core:brand_by_category_new", {"category": "mobiles"}),
    ],
)
@pytest.mark.django_db
def test_core_get_views_status(client, url_data):
    url = reverse(url_data[0], kwargs=url_data[1])
    response = client.get(url)
    assert response.status_code == 200
