from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.container import CONTAINER
from utils.constants import TEMPLATES_DIR

TAG = "news"
PREFFIX = f"/{TAG}"


router = APIRouter(prefix=PREFFIX, tags=[TAG])

templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get("", response_class=HTMLResponse)
async def get_news(request: Request) -> "HTMLResponse":
    """Получить новости."""
    adapter = CONTAINER.news_adapter()
    news = await adapter.get_all()

    return templates.TemplateResponse("news.html", {"request": request, "news": news})


@router.get("/{id}", response_class=HTMLResponse)
async def get_news_item(request: Request, id: int) -> "HTMLResponse":
    """Получить новость."""
    adapter = CONTAINER.news_adapter()
    news_item = await adapter.get(id=id)

    return templates.TemplateResponse(
        "news_item.html", {"request": request, "news_item": news_item}
    )
