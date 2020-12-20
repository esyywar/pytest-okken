from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

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