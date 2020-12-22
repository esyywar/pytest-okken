import pytest
import time
import random
import datetime


@pytest.fixture(autouse=True)
def check_duration(request, cache):
    # To cache duration of each test case (nodeid is unique for each test run)
    key = 'duration/' + request.node.nodeid.replace(':', '_')

    start_time = datetime.datetime.now()

    yield

    stop_time = datetime.datetime.now()

    this_dur = (stop_time - start_time).total_seconds()
    last_dur = cache.get(key, None)
    cache.set(key, this_dur)

    if last_dur is not None:
        error_str = 'Test duration is over 2x more than previous run'
        assert this_dur <= 2 * last_dur, error_str


@pytest.mark.parametrize('i', range(5))
def test_slow(i):
    time.sleep(random.random())