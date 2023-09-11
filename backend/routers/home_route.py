from fastapi import APIRouter, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException

router = APIRouter()

templates = Jinja2Templates(directory="frontend/templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Define a context dictionary with variables to pass to the template
    context = {"message": "Hello, World!"}

    # Render the template with the context
    return templates.TemplateResponse("index.html", {"request": request, **context})
