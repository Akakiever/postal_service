import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestOrderApi:
    def test_get_order(self, example_order, api_client):
        url = reverse('api-v1:orders-detail', args=[example_order.id])
        response = api_client.get(url)
        response_json = response.json()
        assert response.status_code == 200
        assert response_json['id'] == example_order.id
        assert response_json['foreign_id'] == example_order.foreign_id
        assert response_json['location_from'] == example_order.location_from
        assert response_json['location_to'] == example_order.location_to
        assert response_json['status'] == example_order.status
        assert 'datetime_created' in response_json
        assert 'datetime_changed' in response_json

    def test_get_order_list(self, example_order, api_client):
        url = reverse('api-v1:orders-list')
        response = api_client.get(url)
        response_json = response.json()
        assert response.status_code == 200
        assert len(response_json) > 0
        response_order = response_json[0]
        assert 'id' in response_order
        assert 'foreign_id' in response_order
        assert 'location_from' in response_order
        assert 'location_to' in response_order
        assert 'status' in response_order
        assert 'datetime_created' in response_order
        assert 'datetime_changed' in response_order

    def test_create_order(self, api_client):
        url = reverse('api-v1:orders-list')
        data = {
            'foreign_id': 1,
            'location_from': 'foo',
            'location_to': 'bar',
        }
        response = api_client.post(url, data)
        assert response.status_code == 201
        response_json = response.json()
        assert 'id' in response_json

    def test_update_order(self, example_order, api_client):
        url = reverse('api-v1:orders-detail', args=[example_order.id])
        data = {
            'foreign_id': 1,
            'location_from': 'foo',
            'location_to': 'bar',
        }
        response = api_client.patch(url, data)
        assert response.status_code == 200
        example_order.refresh_from_db()
        assert example_order.foreign_id == 1
        assert example_order.location_from == 'foo'
        assert example_order.location_to == 'bar'


