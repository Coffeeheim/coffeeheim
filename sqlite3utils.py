import sqlite3
from datetime import datetime

from pytz import timezone

_TZ = 'America/Sao_Paulo'


def create_table(
    table_name: str,
    conn: sqlite3.Connection,
):
    cursor = conn.cursor()
    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {table_name} \
            (steamid64 TEXT UNIQUE, create_date DATETIME)',
    )

    conn.commit()


def write_row(table_name: str, rowdict: dict, conn: sqlite3.Connection):
    cursor = conn.cursor()
    now = datetime.now(tz=timezone(_TZ))

    rowdict = rowdict | {'create_date': now.isoformat()}
    columns = ','.join(rowdict.keys())
    params = ','.join(['?'] * len(rowdict))
    values = list(rowdict.values())

    cursor.execute(
        f'INSERT INTO {table_name} ({columns}) VALUES ({params})',
        values,
    )

    conn.commit()
