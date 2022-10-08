from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from utils.constants import BASE_DIR


TAG = "index"
PREFIX = ""

router = APIRouter(prefix=PREFIX, tags=[TAG])
templates = Jinja2Templates(directory=BASE_DIR / "app" / "templates")


@router.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("admin/index.html", {"request": request})
