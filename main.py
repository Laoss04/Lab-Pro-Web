from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

product_list = [
    {"ID": 1, "Name": "Product 1", "Price": 10.99},
    {"ID": 2, "Name": "Product 2", "Price": 19.99},
    {"ID": 3, "Name": "Product 3", "Price": 29.99}
]

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"text": "Welcome to the store"}
    )

@app.get("/products", response_class=HTMLResponse)
def products(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="products.html",
        context={"product_list": product_list}
    )

"""
def home(request: Request):

    text = {
        "title": "Home page",
        "content": "boh",
    }
    dictionary = {"key1": "value1", "key2": "value2"}
    context = {"text": text, "dictionary": dictionary}
    return templates.TemplateResponse(
        request = request,
        name="home.html",
        context=context
    )
"""
