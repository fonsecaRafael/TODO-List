from django.test import Client
from django.urls import reverse
import pytest

from todoapp.tasks.models import Tasks


@pytest.fixture
def task(db):
    return Tasks.objects.create(name='Task 1', done=True)


@pytest.fixture
def response(client: Client, task):
    return client.post(reverse('tasks:delete', kwargs={'task_id': task.id}))


def test_delete_task(response):
    assert not Tasks.objects.exists()
