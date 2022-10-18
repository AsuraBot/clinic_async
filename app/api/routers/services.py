from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.container import CONTAINER
from utils.constants import TEMPLATES_DIR

TAG = "services"
PREFFIX = f"/{TAG}"


router = APIRouter(prefix=PREFFIX, tags=[TAG])

templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get("", response_class=HTMLResponse)
async def get_services(request: Request) -> "HTMLResponse":
    """Получить услуги."""
    adapter = CONTAINER.services_adapter()
    services = await adapter.get_all(on_main=False)

    return templates.TemplateResponse(
        "services.html", {"request": request, "services": services}
    )


@router.get("/{id}", response_class=HTMLResponse)
async def get_service(request: Request, id: int) -> "HTMLResponse":
    """Получить услугу."""
    adapter = CONTAINER.services_adapter()
    service = await adapter.get(id=id)

    return templates.TemplateResponse(
        "service.html", {"request": request, "service": service}
    )
