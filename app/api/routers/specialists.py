from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.container import CONTAINER
from utils.constants import TEMPLATES_DIR

TAG = "specialists"
PREFFIX = f"/{TAG}"


router = APIRouter(prefix=PREFFIX, tags=[TAG])

templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get("", response_class=HTMLResponse)
async def get_specialists(request: Request) -> "HTMLResponse":
    """Получить специалистов."""
    adapter = CONTAINER.specialists_adapter()
    specialists = await adapter.get_all(on_main=False)

    return templates.TemplateResponse(
        "specialists.html", {"request": request, "specialists": specialists}
    )


@router.get("/{id}", response_class=HTMLResponse)
async def get_specialist(request: Request, id: int) -> "HTMLResponse":
    """Получить специалиста."""
    adapter = CONTAINER.specialists_adapter()
    specialist = await adapter.get(id=id)

    return templates.TemplateResponse(
        "specialist.html", {"request": request, "specialist": specialist}
    )
