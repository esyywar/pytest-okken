import pytest
import json


@pytest.fixture(scope='module')
def author_file_init(tmpdir_factory):
    author_dir = tmpdir_factory.mktemp('authors')

    author_data = {
        'Archer': {'City': 'London'},
        'Rand': {'City': 'Moscow'},
        'Faulkner': {'City': 'Mississippi'}
    }

    author_file = author_dir.join('author_data.json')

    with author_file.open('w') as author_json:
        json.dump(author_data, author_json)

    return author_file

    

