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


def test_add_returns_valid_id():
    """tasks.add(<valid_task>) should return an id int"""
    t = Task('some job')
    task_id = tasks.add(t)

    assert(isinstance(task_id, int))


@pytest.mark.smoke
def test_added_task_has_id_set():
    """task_id field must be set by tasks.add()"""

    my_task = Task('some job', 'rahul', True)
    task_id = tasks.add(my_task)

    task_from_db = tasks.get(task_id)

    assert(task_from_db.id == task_id)
