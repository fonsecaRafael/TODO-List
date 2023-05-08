from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertContains


@pytest.fixture
def response(client: Client):
    return client.get(reverse('tasks:home'))


def test_status_code(response):
    assert response.status_code == 200


def test_form_is_present(response):
    assertContains(response, '<form')
