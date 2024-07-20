import json
import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

@app.get('/status.json', response_class=JSONResponse)
async def status(request: Request):
    path = 'valheim-server/data/htdocs/status.json'
    content = {}

    if os.path.exists(path):
        with open(path) as f:
            content = json.load(f)

    return JSONResponse(content=content)