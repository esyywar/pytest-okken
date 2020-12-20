from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_asdict():
    """asdict command should return as a dict"""
    t_task = Task('some job', 'rahul', True, 21)
    t_dict = t_task._asdict()

    expected = {
        'summary': 'some job',
        'owner': 'rahul',
        'done': True,
        'id': 21
    }

    assert(t_dict == expected)


def test_replace():
    """replace should change indicated fields"""
    t_before = Task('finish book', 'rahul', False)
    t_after = t_before._replace(id = 10, done = True)

    t_expected = Task('finish book', 'rahul', True, 10)

    assert(t_after == t_expected)