from urllib.parse import urlparse

import steam.steamid as steamid


def uri_validator(url: str) -> bool:
    """
    >>> uri_validator('test')
    False
    >>> uri_validator('https://steamcommunity.com/id/sergiors')
    True
    """
    try:
        r = urlparse(url)
        return all([r.scheme, r.netloc])
    except Exception:
        return False


def get_steamid_64(username: str) -> int:
    """
    >>> get_steamid_64('sergiors')
    76561198096312074

    >>> get_steamid_64('https://steamcommunity.com/id/sergiors')
    76561198096312074

    >>> get_steamid_64('')
    Traceback (most recent call last):
      ...
    ValueError: User not found.
    """
    if not uri_validator(username):
        username = f'https://steamcommunity.com/id/{username}'

    sid = steamid.from_url(username)

    if not sid:
        raise ValueError('User not found.')

    return sid.as_64


if __name__ == '__main__':
    import doctest

    doctest.testmod()
