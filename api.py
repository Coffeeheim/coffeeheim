from http import HTTPStatus
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fileutils import json_content

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


@app.get('/status.json')
async def status():
    return JSONResponse(
        content=json_content('valheim-server/data/htdocs/status.json'),
    )
