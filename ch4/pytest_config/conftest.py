import pytest


def pytest_addoption(parser):
    parser.addoption("--myopt", action="store_true", help="some boolean option")
    parser.addoption("--foo", action="store", default="bar", help="foo: bar or baz")


@pytest.fixture()
def get_myopt(pytestconfig):
    return pytestconfig.option.myopt


@pytest.fixture()
def get_foo(pytestconfig):
    return pytestconfig.option.foo