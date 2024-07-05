from tempfile import NamedTemporaryFile

import pytest

import fileutils


def test_append_row_steamid():
    with NamedTemporaryFile() as fp:
        assert fileutils.append_row(fp.name, '123')


def test_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        fileutils.append_row('/permittedlist.txt', '123')
