from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import admin

from utils.constants import BASE_DIR


STATIC_PREFIX = "/static"


def create_app() -> "FastAPI":
    """Создать приложение FastAPI."""
    app = FastAPI(docs_url=None, redoc_url=None)

    # Подключение админ-панели.
    admin.create_app(app)

    # Подключение подприложений.
    static_files = StaticFiles(directory=BASE_DIR / "app" / "static")
    app.mount(STATIC_PREFIX, static_files, name="static")

    return app
