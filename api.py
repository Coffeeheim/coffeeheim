import json
from http import HTTPStatus
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()


@app.get('/logs', response_class=JSONResponse)
async def logs(f: str = ''):
    basepath = Path('logs')
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
        return PlainTextResponse(content=filepath.read_text())

    content = []
    for file in filepath.iterdir():
        if file.suffix == '.meta':
            continue
        content.append(file.name if file.is_file() else f'{file.name}/')

    return JSONResponse(content=content)


@app.get('/status.json', response_class=JSONResponse)
async def status():
    filepath = Path('valheim-server/data/htdocs/status.json')
    content = {}

    if filepath.exists():
        with filepath.open() as f:
            content = json.load(f)

    return JSONResponse(content=content)
