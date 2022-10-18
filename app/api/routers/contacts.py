from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.container import CONTAINER
from utils.constants import TEMPLATES_DIR

TAG = "contacts"
PREFFIX = f"/{TAG}"


router = APIRouter(prefix=PREFFIX, tags=[TAG])

templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get("", response_class=HTMLResponse)
async def get_contacts(request: Request) -> "HTMLResponse":
    """Получить контакты."""
    adapter = CONTAINER.contacts_adapter()
    contacts = await adapter.get_all()

    return templates.TemplateResponse(
        "contacts.html", {"request": request, "contacts": contacts}
    )
