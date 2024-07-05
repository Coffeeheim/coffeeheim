from urllib.parse import urlparse

import steam.steamid as steamid


def uri_validator(url: str) -> bool:
    try:
        r = urlparse(url)
        return all([r.scheme, r.netloc])
    except Exception:
        return False


def get_steamid_64(username: str) -> int:
    if not uri_validator(username):
        username = f'https://steamcommunity.com/id/{username}'

    sid = steamid.from_url(username)

    if not sid:
        raise ValueError('User not found.')

    return sid.as_64
