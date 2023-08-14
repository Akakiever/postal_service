from unittest import mock

import pytest

from app.models import Order
from app.tasks import change_order_status_delivered, change_order_status_random


@pytest.mark.django_db
class TestChangeOrderStatusDelivered:
    def test_task(self, example_order):
        with mock.patch(
                'app.tasks.change_order_status_random.apply_async') as task_mock:
            change_order_status_delivered(example_order.id)
            example_order.refresh_from_db()
            assert example_order.status == Order.OrderStatus.DELIVERED.value
            assert task_mock.call_count == 1


@pytest.mark.django_db
class TestChangeOrderStatusRandom:
    def test_task(self, example_order):
        change_order_status_random(example_order.id)
        example_order.refresh_from_db()
        assert example_order.status in (
            Order.OrderStatus.RECEIVED.value,
            Order.OrderStatus.REJECTED.value,
        )