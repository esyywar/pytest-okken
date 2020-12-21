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
