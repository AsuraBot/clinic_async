from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api import admin
from app.api import root
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

    root_api = root.create_app()
    app.mount(root.PREFIX, root_api)

    return app
