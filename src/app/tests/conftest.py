import pytest
from django.test import Client
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture()
def api_client():
    client = APIClient()
    return client


@pytest.fixture()
def client():
    client = Client()
    return client


@pytest.fixture
def example_order():
    return baker.make('Order')
