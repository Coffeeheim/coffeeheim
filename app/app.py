import json
import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount('/assets', StaticFiles(directory='app/assets'), name='assets')

templates = Jinja2Templates(directory='app/templates')


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='index.html',
    )


@app.get('/status', response_class=JSONResponse)
async def status(request: Request):
    path = 'data/htdocs/status.json'
    content = {}

    if os.path.exists(path):
        with open(path) as f:
            content = json.load(f)

    return JSONResponse(content=content)
