from fastapi import APIRouter, Request
from app.container import CONTAINER
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from utils.constants import BASE_DIR

TAG = "specialists"
PREFFIX = f"/{TAG}"


router = APIRouter(prefix=PREFFIX, tags=[TAG])

templates = Jinja2Templates(directory=BASE_DIR / "app" / "templates")


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
        "specialists.html", {"request": request, "specialist": specialist}
    )
