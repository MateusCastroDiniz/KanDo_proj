# from functools import reduce
#
# import pytest
# from core.KanDo.factories import *
#
#
#
# @pytest.fixture
# def task_published():
#     ColumnFactory(column_name='sla')
#     return TaskFactory(column=Column.objects.get(column_name='sla'))
#
#
# @pytest.mark.django_db
# def test_create_published_post(task_published):
#     assert task_published.column == 'sla'
