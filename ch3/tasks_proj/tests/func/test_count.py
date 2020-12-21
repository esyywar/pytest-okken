import pytest
import tasks
from tasks import Task


def test_count(db_4_tasks):
    """Connected 4 task db should have 4 tasks"""
    assert(tasks.count() == 4)


def test_count_inc(db_4_tasks):
    """Adding task to 4 task db should increment count"""
    t = Task('some job', 'Mark')
    tasks.add(t)

    assert(tasks.count() == 5)