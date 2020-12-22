import pytest
import os

import players


def test_players_data(tmpdir, monkeypatch):
    """Write players data and check the file"""
    test_dir = tmpdir.mkdir('home')
    monkeypatch.setattr(os.path, "expanduser", lambda x: x.replace("~", str(test_dir)))

    players.write_default_player_prefs()
    expected = players.default_players
    actual = players.read_player_prefs()
    assert actual == expected