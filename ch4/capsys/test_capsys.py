import pytest
import sys


def greeting(name):
    print('Hello, {}.'.format(name))


def test_greeting(capsys):
    greeting('Rahul')
    out, err = capsys.readouterr()
    assert out == 'Hello, Rahul.\n'
    assert err == ''

    greeting('Carter')
    greeting('Steve')
    out, err = capsys.readouterr()
    assert out == 'Hello, Carter.\nHello, Steve.\n'
    assert err == ''


def yikes(problem):
    # Print to err stream instead of stdout
    print('Yikes! {}'.format(problem), file=sys.stderr)


def test_yikes(capsys):
    yikes('Dog got out!')
    out, err = capsys.readouterr()
    assert out == ''
    assert 'Dog got out!' in err