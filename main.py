from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    text = {
        "title": "Home page",
        "content": "boh",
    }
    context = {"text": text, "sequence": ["a", "b", "c"]}
    return templates.TemplateResponse(
        request = request,
        name="home.html",
        context=context
    )