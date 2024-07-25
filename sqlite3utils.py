import os
import sqlite3
from contextlib import closing
from datetime import datetime

from pytz import timezone

TZ: str = os.environ.get('TZ')  # type: ignore


class SQLite:
    def __init__(self, database):
        self.database = database

    def __enter__(self):
        self.conn = sqlite3.connect(self.database)
        return self.conn.cursor()

    def __exit__(self, exc_type, exc, exc_tb):
        self.conn.commit()
        self.conn.close()


def create_table(
    table_name: str,
    conn: sqlite3.Connection,
):
    with closing(conn.cursor()) as cursor:
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                steamid64 TEXT UNIQUE NOT NULL,
                banned BOOL DEFAULT 0,
                admin BOOL DEFAULT 0,
                last_login DATETIME,
                create_date DATETIME NOT NULL
            )
            """
        )

    conn.commit()


def write_row(
    table_name: str,
    rowdict: dict,
    conn: sqlite3.Connection,
    *,
    tz: str = TZ,
):
    current_time = datetime.now(tz=timezone(tz))
    rowdict = rowdict | {'create_date': current_time.isoformat()}
    columns = ','.join(rowdict.keys())
    params = ','.join(['?'] * len(rowdict))
    values = list(rowdict.values())

    with conn as cursor:
        cursor.execute(
            f'INSERT INTO {table_name} ({columns}) VALUES ({params})',
            values,
        )

    conn.commit()
