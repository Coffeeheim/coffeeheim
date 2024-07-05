from urllib.parse import urlparse

import steam.steamid as steamid
from aws_lambda_powertools.event_handler.exceptions import NotFoundError


def uri_validator(url: str) -> bool:
    try:
        r = urlparse(url)
        return all([r.scheme, r.netloc])
    except Exception:
        return False


def get_steamid_64(username: str) -> str:
    if username.isdigit() and len(username) == 17:
        return username

    if not uri_validator(username):
        username = f'https://steamcommunity.com/id/{username}'

    sid = steamid.from_url(username)

    if not sid:
        raise NotFoundError('User not found.')

    return str(sid.as_64)
