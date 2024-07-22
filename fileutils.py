import json
from pathlib import Path


def append_row(filepath: str, steamid: str) -> bool | None:
    filepath_ = Path(filepath)
    if not filepath_.exists():
        raise FileNotFoundError

    with filepath_.open('a') as f:
        try:
            f.write(f'{steamid}\n')
        except Exception:
            return None
        else:
            return True


def json_content(filepath: str) -> dict:
    filepath_ = Path(filepath)

    if not filepath_.exists():
        return {}

    with filepath_.open() as fp:
        return json.load(fp)
