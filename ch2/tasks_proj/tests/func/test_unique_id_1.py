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


@pytest.mark.skipif(tasks.__version__ < '0.2.0', reason='not testable till version 0.2.1')
def test_unique_id():
    """Calling unique_id() twice should give different ints"""
    id1 = tasks.unique_id()
    id2 = tasks.unique_id()

    assert(id1 != id2)


def test_unique_id_2():
    """unique_id should return int of id ununsed in db"""
    ids = []
    ids.append(tasks.add(Task('one job')))
    ids.append(tasks.add(Task('second job')))
    ids.append(tasks.add(Task('third job')))

    uuid = tasks.unique_id()

    assert(uuid not in ids)