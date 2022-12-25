from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from utils.constants import MAIN_TEMPLATES_DIR

TAG = "index"
PREFFIX = ""


router = APIRouter(prefix=PREFFIX, tags=[TAG])

templates = Jinja2Templates(directory=MAIN_TEMPLATES_DIR)


@router.get("/", response_class=HTMLResponse)
async def get_index(request: Request) -> "HTMLResponse":
    """Получить главную страницу."""

    return templates.TemplateResponse("index.html", {"request": request})
