from tempfile import NamedTemporaryFile

import pytest

import fileutils


def test_append_row_steamid():
    with NamedTemporaryFile() as fp:
        assert fileutils.append_row(fp.name, '123')


def test_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        fileutils.append_row('/permittedlist.txt', '123')


def test_json_content():
    expected = {'last_status_update': '2024-07-22T17:19:49.515439+00:00'}
    assert expected == fileutils.json_content('tests/sample.json')
