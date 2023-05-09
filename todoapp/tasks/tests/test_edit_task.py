from django.test import Client
from django.urls import reverse
import pytest

from todoapp.tasks.models import Tasks


@pytest.fixture
def pending_task(db):
    return Tasks.objects.create(name='Task 1', done=False)


@pytest.fixture
def response_pending_task(client: Client, pending_task):
    return client.post(
        reverse('tasks:detail', kwargs={'task_id': pending_task.id}),
        data={'done': 'true', 'name': f'{pending_task.name}-editada'}
    )


def test_status_code(response_pending_task):
    assert response_pending_task.status_code == 302


def test_done_task(response_pending_task):
    assert Tasks.objects.first().done


@pytest.fixture
def done_task(db):
    return Tasks.objects.create(name='Task 1', done=True)


@pytest.fixture
def response_done_task(client: Client, done_task):
    return client.post(
        reverse('tasks:detail', kwargs={'task_id': done_task.id}),
        data={'name': f'{done_task.name}-editada'}
    )


def test_pending_task(response_done_task):
    assert not Tasks.objects.first().done
