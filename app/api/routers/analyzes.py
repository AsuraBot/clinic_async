from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.container import CONTAINER
from utils.constants import TEMPLATES_DIR

TAG = "analyzes"
PREFFIX = f"/{TAG}"


router = APIRouter(prefix=PREFFIX, tags=[TAG])

templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get("", response_class=HTMLResponse)
async def get_analyzes(request: Request) -> "HTMLResponse":
    """Получить анализы."""
    adapter = CONTAINER.analyzes_adapter()
    analyzes = await adapter.get_all(on_main=False)

    return templates.TemplateResponse(
        "analyzes.html", {"request": request, "analyzes": analyzes}
    )


@router.get("/{id}", response_class=HTMLResponse)
async def get_analysis(request: Request, id: int) -> "HTMLResponse":
    """Получить анализ."""
    adapter = CONTAINER.analyzes_adapter()
    analysis = await adapter.get(id=id)

    return templates.TemplateResponse(
        "analysis.html", {"request": request, "analysis": analysis}
    )
