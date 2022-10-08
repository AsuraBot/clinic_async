from utils.constants import BASE_DIR
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import admin


def create_app() -> "FastAPI":
    """Создать приложение FastAPI."""
    app = FastAPI(title="clinic", version="0.1.0", redoc_url=None)

    # Подключение подприложения.
    admin_panel = admin.create_app(title="Административная панель", version="0.1.0")
    app.mount(admin.PREFIX, admin_panel, name="admin")

    static_files = StaticFiles(directory=BASE_DIR / "app" / "static")
    app.mount("/static", static_files, name="static")

    return app
