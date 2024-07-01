from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory='web/assets'), name='assets')

templates = Jinja2Templates(directory='web/templates')


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    users = [{'username': 'Mandrake'}]
    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context={'users': users},
    )
