from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    html = """
    <!DOCTYPE html>
    <html>
        <body>
            <h1>Halo</h1>
            <p>idk</p>
        </body>
    </html>
    """
    return html