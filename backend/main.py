from fastapi import FastAPI

from backend.routers import blogs
from .routers import openai_route, blogs
import uvicorn
from fastapi import HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException

app = FastAPI()

app.include_router(openai_route.router)
app.include_router(blogs.router)

# Mount the static files directory
app.mount("/frontend/", StaticFiles(directory="./frontend/static"), name="static")

# Create an instance of the Jinja2Templates class
templates = Jinja2Templates(directory="frontend/templates")


# Define a custom error handler for 404 errors
@app.exception_handler(HTTPException)
async def not_found_error_handler(request: Request, exc: HTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse(
            "404.html", {"request": request}, status_code=404
        )
    return exc


def start():
    uvicorn.run("backend.main:app", port=8888, reload=True)
