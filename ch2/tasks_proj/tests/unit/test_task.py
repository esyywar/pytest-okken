from tasks import Task


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


def test_defaults():
    """No params, invoke defaults"""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert(t1 == t2)


def test_member_access():
    """Check fields of namedtuple"""
    t = Task('buy milk', 'brian')

    assert(t.summary == 'buy milk')
    assert(t.owner == 'brian')
    assert((t.done, t.id) == (False, None))
