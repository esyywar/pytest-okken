import pytest  
import tasks
from tasks import Task


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