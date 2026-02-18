from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body>
            <h1>CI/CD Demo App</h1>
            <p>If tests pass, this page gets deployed 🚀</p>
        </body>
    </html>
    """

@app.get("/add")
def add(a:int , b:int):
    return {"result": a+b} #returning a JSON object