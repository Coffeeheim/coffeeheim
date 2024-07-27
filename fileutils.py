import json
from pathlib import Path


def append_row(rawpath: str, s: str) -> bool | None:
    filepath = Path(rawpath)

    if not filepath.exists():
        raise FileNotFoundError

    with filepath.open('a') as f:
        try:
            f.write(f'{s}\n')
        except Exception:
            return None
        else:
            return True


def json_content(rawpath: str) -> dict:
    filepath = Path(rawpath)

    if not filepath.exists():
        return {}

    with filepath.open() as fp:
        return json.load(fp)
