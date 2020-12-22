import json


def test_archer_london(author_file_init):
    """Test that Archer is in city of London in author data"""
    with author_file_init.open() as author_json:
        authors = json.load(author_json)

    assert(authors['Archer']['City'] == 'London')


def test_authors_have_cities(author_file_init):
    """All authors should have city data"""
    with author_file_init.open() as author_json:
        authors = json.load(author_json)

    for name in authors:
        assert(authors[name].get('City'))