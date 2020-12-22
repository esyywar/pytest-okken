import pytest


def test_option(pytestconfig, get_myopt, get_foo):
    print('"myopt" set to: ', get_foo)
    print('"foo" set to: ', get_foo)
    