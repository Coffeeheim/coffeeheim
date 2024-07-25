import os
from http import HTTPStatus
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fileutils import json_content
from sqlite3utils import SQLite

DATABASE_FILE: str = os.environ.get('DATABASE_FILE')  # type: ignore

app = FastAPI()


@app.get('/logs')
async def logs(f: str = ''):
    dirname = 'logs/'
    basepath = Path(dirname)
    filepath = basepath / f

    try:
        filepath.relative_to(basepath)
    except ValueError:
        return JSONResponse(
            content=None,
            status_code=HTTPStatus.FORBIDDEN,
        )

    if not filepath.exists():
        return JSONResponse(
            content=None,
            status_code=HTTPStatus.NOT_FOUND,
        )

    if filepath.is_file():
        return FileResponse(filepath)

    files = []
    for file in filepath.iterdir():
        if file.suffix == '.meta':
            continue
        filepath = str(file).removeprefix(dirname)
        files.append(filepath if file.is_file() else f'{filepath}/')

    return JSONResponse(content=files)


@app.get('/players')
async def players():
    with SQLite(DATABASE_FILE) as cur:
        cur.execute(f'SELECT * FROM permittedlist ORDER BY create_date DESC')
        columns = [x[0] for x in cur.description]
        content = [dict(zip(columns, x)) for x in cur.fetchall()]

        return JSONResponse(content=content)


@app.get('/status')
async def status():
    return JSONResponse(
        content=json_content('valheim-server/data/htdocs/status.json'),
    )
