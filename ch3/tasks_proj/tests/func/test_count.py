import pytest
import tasks
from tasks import Task


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