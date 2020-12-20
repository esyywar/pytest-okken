import pytest 
from tasks import Task


@pytest.mark.xfail()
def test_task_equality():
    """Different tasks are not equal"""
    t1 = Task('this job', 'john')
    t2 = Task('that task', 'rahul')

    assert(t1 == t2)


@pytest.mark.xfail()
def test_dict_equality():
    """Diff tasks as dicts not equal"""
    t1 = Task('this job', 'john')._asdict()
    t2 = Task('that task', 'rahul')._asdict()

    assert t1 == t2