import pytest
import tasks 
from tasks import Task


@pytest.mark.smoke
def test_list_raises():
    """list() fails when owner input is not string"""
    with pytest.raises(TypeError):
        tasks.list_tasks(42)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """list() fails when id input is not int"""
    with pytest.raises(TypeError):
        tasks.get("not an id")
        tasks.get(None)
        tasks.get([1])


def test_add_raises():
    """add() raises exception if param is not a Task type"""
    with pytest.raises(TypeError):
        tasks.add(task='not a task')


def test_add_raises_2():
    """add() raises exception if given task with an id"""
    with pytest.raises(ValueError):
        tasks.add(Task('some job', 'rahul', False, 42))


def test_start_tasks_db_raises():
    """Unsupported dbs raise exception"""
    with pytest.raises(ValueError) as excInfo:
        tasks.start_tasks_db('some/path', 'invalid_db')
    
    print(excInfo)
    excMsg = excInfo.value.args[0]

    assert(excMsg == "db_type must be a 'tiny' or 'mongo'")


class TestUpdate():
    """Test exceptions with tasks.update()"""

    def test_bad_id(self):
        """Non int task id should raise exception"""
        with pytest.raises(TypeError):
            tasks.update('not an id', Task('some job'))

    def test_bad_task(self):
        """Giving non-task should raise exception"""
        with pytest.raises(TypeError):
            tasks.update(5, 'not a task')
