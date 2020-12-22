import pytest
from pytest import approx


test_data = (
    (1.01, 2.01, 3.02),
    (1e25, 1e23, 1.1e25),
    (1.23, 3.21, 4.44),
    (0.1, 0.2, 0.3),
    (1e25, 1e24, 1.1e25)
)


def test_pass():
    assert 1 == 1


def test_fail():
    assert 1 == 2


@pytest.mark.parametrize("x, y, expected", test_data)
def test_sums(x, y, expected):
    """Use approx() to check sum of two floats"""
    result = x + y
    assert(result == approx(expected))
