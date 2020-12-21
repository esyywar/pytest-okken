import pytest
import tasks
from tasks import Task


@pytest.mark.xfail(reason='uuid is not a string')
def test_unique_id_is_duck():
    """Check if uuid is a string"""
    uuid = tasks.unique_id()
    assert(uuid == 'duck')


@pytest.mark.xfail(reason='demonstrate XPASS')
def test_unique_id_not_duck():
    """Demonstrate XPASS by checking if uuid is a string"""
    uuid = tasks.unique_id()
    assert(uuid != 'duck')