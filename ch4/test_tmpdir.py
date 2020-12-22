import pytest

def test_tmpdir_factory(tmpdir_factory):
    a_dir = tmpdir_factory.mktemp('mydir')

    a_file = a_dir.join('sample.txt')

    a_sub_dir = a_dir.mkdir('subdir')
    another_file = a_sub_dir.join('another_sample.txt')

    a_file.write('This sample is the original.')
    another_file.write('This sample is the second of its kind.')

    assert(a_file.read() == 'This sample is the original.')
    assert(another_file.read() == 'This sample is the second of its kind.')