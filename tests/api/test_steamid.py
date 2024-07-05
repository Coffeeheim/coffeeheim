import pytest

import api.steamid as steamid


def test_uri_validator():
    assert steamid.uri_validator('https://steamcommunity.com/id/sergiors')
    assert steamid.uri_validator('test') == False


def test_get_steamid_64_value():
    assert steamid.get_steamid_64('sergiors')
    assert steamid.get_steamid_64('https://steamcommunity.com/id/sergiors')


def test_get_steamid_64_value_error():
    with pytest.raises(ValueError):
        steamid.get_steamid_64('')
