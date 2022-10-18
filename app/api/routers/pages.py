from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.container import CONTAINER
from utils.constants import TEMPLATES_DIR

TAG = "pages"
PREFFIX = f"/{TAG}"


router = APIRouter(prefix=PREFFIX, tags=[TAG])

templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get("/{slug}", response_class=HTMLResponse)
async def get_page(request: Request, slug: str) -> "HTMLResponse":
    """Получить страницу."""
    adapter = CONTAINER.pages_adapter()
    page = await adapter.get(slug=slug)

    return templates.TemplateResponse("page.html", {"request": request, "page": page})
