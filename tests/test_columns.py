from functools import reduce

import pytest
from core.KanDo.factories import *


@pytest.fixture
def column_published():
    return ColumnFactory(column_name='sla')


@pytest.mark.django_db
def test_create_column(column_published):
    assert column_published.column_name == 'sla'
