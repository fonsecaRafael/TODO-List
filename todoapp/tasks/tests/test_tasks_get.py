from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertContains

from todoapp.tasks.models import Tasks


@pytest.fixture
def response(client: Client, db):
    return client.get(reverse('tasks:home'))


def test_status_code(response):
    assert response.status_code == 200


def test_form_is_present(response):
    assertContains(response, '<form')


@pytest.fixture
def pending_tasks_list(db):
    tasks = [
        Tasks(name='Task 1', done=False),
        Tasks(name='Task 2', done=False),
    ]

    Tasks.objects.bulk_create(tasks)
    return tasks


@pytest.fixture
def done_tasks_list(db):
    tasks = [
        Tasks(name='Task 3', done=True),
        Tasks(name='Task 4', done=True),
    ]

    Tasks.objects.bulk_create(tasks)
    return tasks


@pytest.fixture
def response_tasks_list(client: Client, pending_tasks_list, done_tasks_list):
    return client.get(reverse('tasks:home'))


def test_pending_tasks_list_is_present(response_tasks_list, pending_tasks_list):
    for task in pending_tasks_list:
        assertContains(response_tasks_list, task.name)


def test_done_tasks_list_is_present(response_tasks_list, done_tasks_list):
    for task in done_tasks_list:
        assertContains(response_tasks_list, task.name)
