from tempfile import NamedTemporaryFile

import pytest

import permittedlist


def test_append_steamid():
    with NamedTemporaryFile() as fp:
        assert permittedlist.append(fp.name, '123')


def test_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        permittedlist.append('/permittedlist.txt', '123')
