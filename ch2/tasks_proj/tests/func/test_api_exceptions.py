import pytest
import tasks 

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


def test_start_tasks_db_raises():
    """Unsupported dbs raise exception"""
    with pytest.raises(ValueError) as excInfo:
        tasks.start_tasks_db('some/path', 'invalid_db')
    
    print(excInfo)
    excMsg = excInfo.value.args[0]

    assert(excMsg == "db_type must be a 'tiny' or 'mongo'")