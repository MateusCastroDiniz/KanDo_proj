import pytest
from core.KanDo.factories import *

@pytest.fixture
def board_created():
    return BoardFactory(board_name='myboard')

@pytest.mark.django_db
def test_create_postbycolumn(board_created):
    assert board_created.board_name == 'myboard'

