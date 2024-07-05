import os


def append_row(path: str, steamid: str) -> bool | None:
    if not os.path.exists(path):
        raise FileNotFoundError

    with open(path, 'a') as f:
        try:
            f.write(f'{steamid}\n')
        except Exception:
            return None
        else:
            return True
