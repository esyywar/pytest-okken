import pytest
import time
import random
import datetime

from collections import namedtuple


# curr and last are dictionaries where keys are the nodeids of each test
Duration = namedtuple('Duration', ['curr', 'last'])


@pytest.fixture(scope='session')
def duration_cache(request):
    key = 'duration/testdurations'

    d = Duration({}, request.config.cache.get(key, {}))

    # Instead of returning 'd', we yield 'd' to provide access to 'd' for tests w/o returning
    yield d

    request.config.cache.set(key, d.curr)


@pytest.fixture(autouse=True)
def check_duration(request, duration_cache):
    d = duration_cache
    nodeId = request.node.nodeid

    start_time = datetime.datetime.now()

    yield

    duration = (datetime.datetime.now() - start_time).total_seconds()
    d.curr[nodeId] = duration

    # Assertion fail in fixture gives ERROR and not FAIL
    if d.last.get(nodeId) is not None:
        error_str = 'Test duration is over 2x previous duration.'
        assert duration <= 2 * d.last[nodeId], error_str
    


@pytest.mark.parametrize('i', range(5))
def test_slow(i):
    time.sleep(random.random())