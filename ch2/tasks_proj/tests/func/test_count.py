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


task_count_params = [
    [Task('one job')],
    [Task('one job'), Task('two jobs')],
    [Task('one job'), Task('two jobs'), Task('three jobs')]]


@pytest.mark.parametrize('task_list', task_count_params)
class TestCount():
    """API count should return number of tasks in database"""

    def test_count(self, task_list):
        for task in task_list:
            tasks.add(task)

        num_tasks = tasks.count()

        assert(num_tasks == len(task_list))