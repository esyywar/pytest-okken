import pytest
import tasks
from tasks import Task


task_test_params = [
    Task('sleep', done = True), 
    Task('my job', 'rahul'), 
    Task('go to gym', 'rahul', True),
    Task('go home', 'jeezy', False)]

task_test_params_ids = ["Task({},{},{})".format(t.summary, t.owner, t.done) for t in task_test_params]


def equivalent_tasks(t1, t2):
    """Checking two tasks for equivalence (all fields but id)"""
    return((t1.summary == t2.summary) and (t1.owner == t2.owner) and (t1.done == t2.done))


def test_add_task():
    """Adding task and getting back task by id"""
    t = Task('some job', 'rahul', False)
    t_id = tasks.add(t)

    t_from_db = tasks.get(t_id)

    assert(equivalent_tasks(t, t_from_db))


@pytest.mark.parametrize('task', task_test_params)
def test_add_task_2(task):
    """Parametrized test with 1 param"""
    t_id = tasks.add(task)

    t_from_db = tasks.get(t_id)

    assert(equivalent_tasks(task, t_from_db))


@pytest.mark.parametrize('task', task_test_params, ids = task_test_params_ids)
def test_add_task_3(task):
    """Parametrized test with 1 param"""
    t_id = tasks.add(task)

    t_from_db = tasks.get(t_id)

    assert(equivalent_tasks(task, t_from_db))


@pytest.mark.parametrize('task', task_test_params, ids = task_test_params_ids)
class TestAdd():
    """Demonstrate class parametrized tests"""

    def test_equiv_add_get(self, task):
        """Adding task and getting back task by id inside class"""
        t_id = tasks.add(task)
        t_from_db = tasks.get(t_id)
        assert(equivalent_tasks(task, t_from_db))

    def test_valid_id(self, task):
        """Checking that id of task we get is same as given id"""
        t_id = tasks.add(task)
        t_from_db = tasks.get(t_id)
        assert(t_from_db.id == t_id)

