from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.container import CONTAINER
from utils.constants import TEMPLATES_DIR

TAG = "promotions"
PREFFIX = f"/{TAG}"


router = APIRouter(prefix=PREFFIX, tags=[TAG])

templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get("", response_class=HTMLResponse)
async def get_promotions(request: Request) -> "HTMLResponse":
    """Получить акции."""
    adapter = CONTAINER.promotions_adapter()
    promotions = await adapter.get_all(on_main=False)

    return templates.TemplateResponse(
        "promotions.html", {"request": request, "promotions": promotions}
    )


@router.get("/{id}", response_class=HTMLResponse)
async def get_promotion(request: Request, id: int) -> "HTMLResponse":
    """Получить акцию."""
    adapter = CONTAINER.promotions_adapter()
    promotion = await adapter.get(id=id)

    return templates.TemplateResponse(
        "promotion.html", {"request": request, "promotion": promotion}
    )
