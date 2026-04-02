from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from pydantic import Field, BaseModel

class Product(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=30)]
    price: Annotated[float, Field(gt=0)]
    location: Annotated[str, Field(min_length=3)]

product = Product.model_validate(
    {name}
)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

product_list = [
    {"id": 1, "name": "Product 1", "price": 10.99},
    {"id": 2, "name": "Product 2", "price": 19.99},
    {"id": 3, "name": "Product 3", "price": 29.99}
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

@app.get("/product_form", response_class=HTMLResponse)
def add_product(request: Request,):
    return templates.TemplateResponse(
        request=request,
        name="product_form.html"
    )

@app.post("/insert_product")
def insert_product(
    name: Annotated[str, Form(), Field(min_length=3, max_length=30)],
    price: Annotated[float, Form(), Field(gt=0)],
    location: Annotated[str, Form(), Field(min_length=3)]
):
    new_id = len(product_list) + 1

    product = {"id": new_id, "name": name, "price": price, "location": location}
    product_list.append(product)
    return "Product added successfully"

@app.post("/insert_product_json")
def insert_product_json(
    product: Product
):
    print(product)