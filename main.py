from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world(
    q: str,
    sort: bool = False
    ) -> dict[str, str | bool]:
    return {"q": q, "sort": sort}

@app.get("/home")
def homepage():
    return "This is the homepage"

@app.get("/{username}")
def username_webpage(
    username: str
):
    return f"This is the webpage of user {username}"

@app.get("/{username}/orders/{orders_id}")
def repository_webpage(
    username: str,
    orders_id: int,
    sort: bool = False
):
    return f"Order {orders_id} for user {username}. Sorted: {sort}"