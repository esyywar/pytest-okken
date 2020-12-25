import pytest
import tasks
from tasks import Task


@pytest.fixture(scope='session', autouse=True, params=['tiny'])
def init_tasks_db(tmpdir_factory, request):
    """Connect to db before testing, disconnect after"""
    temp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(temp_dir), request.param)

    # Yield and allow testing to happend
    yield

    # Teardown and stop db instance
    tasks.stop_tasks_db()


@pytest.fixture()
def empty_tasks_db(init_tasks_db):
    """Empties the connected database between test functions"""
    tasks.delete_all()


@pytest.fixture(scope='session')
def task_examples():
    """Tasks with unique summaries and ownders"""
    return (
        Task('Walk the dog', 'Kelly', False),
        Task('Eat cereal', 'Rahul', True),
        Task('Make bread', 'Adi', False),
        Task('Cook dinner', 'Amy', True)
    )


@pytest.fixture(scope='session')
def tasks_mult_per_owner():
    """Several owners with multiple tasks each"""
    return (
        Task('Read a book', 'Rahul', False),
        Task('Write paper', 'Rahul', False),
        Task('Get hype', 'Rahul', True),

        Task('Feed the cat', 'Lily', True),
        Task('Make the bed', 'Lily', True),
        Task('Set yoghurt', 'Lily', False),

        Task('Get shots up', 'Marvin', False),
        Task('Lift weights', 'Marvin', True),
        Task('Get treatment', 'Marvin', False)
    )


@pytest.fixture()
def db_4_tasks(init_tasks_db, empty_tasks_db, task_examples):
    """Connected db with 4 unique tasks"""
    for task in task_examples:
        tasks.add(task)


@pytest.fixture()
def db_mult_per_owner(init_tasks_db, empty_tasks_db, tasks_mult_per_owner):
    """Connected db with multiple tasks for 3 unique owners"""
    for task in tasks_mult_per_owner:
        tasks.add(task)
