import pytest
import tasks
from tasks import Task


@pytest.fixture(autouse = True)
def init_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after"""
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    # Yield and allow testing to happend
    yield

    # Teardown and stop db instance
    tasks.stop_tasks_db()


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