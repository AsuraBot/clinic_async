from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api import admin
from utils.constants import BASE_DIR


def create_app() -> "FastAPI":
    """Создать приложение FastAPI."""
    version = "0.1.0"
    title = "clinic"

    app = FastAPI(title=title, version=version, docs_url=None, redoc_url=None)

    # Подключение подприложения.
    admin_panel = admin.create_app(title=title, version=version)
    app.mount(admin.PREFIX, admin_panel, name="admin")

    static_files = StaticFiles(directory=BASE_DIR / "app" / "static")
    app.mount("/static", static_files, name="static")

    return app
