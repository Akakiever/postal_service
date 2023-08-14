import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestOrders:
    def test_list(self, example_order, client):
        url = reverse('order-list')
        response = client.get(url)
        assert response.status_code == 200
        assert example_order.location_from in response.rendered_content

    def test_detail(self, example_order, client):
        url = reverse('order-detail', kwargs={'pk': example_order.id})
        response = client.get(url)
        assert response.status_code == 200
        assert example_order.location_from in response.rendered_content
