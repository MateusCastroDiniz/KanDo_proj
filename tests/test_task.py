from functools import reduce

import pytest
from core.KanDo.factories import TaskFactory



@pytest.fixture
def task_published():
    return TaskFactory(title='factory')


@pytest.mark.django_db
def test_create_published_post(task_published):
    assert task_published.title == 'factory'
