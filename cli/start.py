import click
import uvicorn

from app.settings.uvicorn import UvicornSettings
from app.adapters.storage.db import engine
from app.adapters.storage.db.base_model import BaseModel
from app.admin.factory import create_app


@click.group()
def start() -> None:
    """Запустить сервис."""


@start.command()
def api() -> None:
    """API сервис."""
    uvicorn.run(**UvicornSettings().dict())


@start.command()
def admin() -> None:
    """Админ сервис."""
    BaseModel.metadata.bind = engine.get()

    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
