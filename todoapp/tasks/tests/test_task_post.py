from django.test import Client
from django.urls import reverse
import pytest
from todoapp.tasks.models import Tasks


@pytest.fixture
def response(client: Client, db):
    return client.post(reverse('tasks:home'), data={'name': 'Task'})


def test_task_exists_in_db(response):
    assert Tasks.objects.exists()


def test_redirect_after_save(response):
    assert response.status_code == 302


@pytest.fixture
def response_invalid_data(client: Client, db):
    return client.post(reverse('tasks:home'), data={'name': ''})


def test_task_not_exists_in_db(response_invalid_data):
    assert not Tasks.objects.exists()


def test_page_with_invalid_data(response_invalid_data):
    assert response_invalid_data.status_code == 400
