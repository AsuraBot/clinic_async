from fastapi import FastAPI

from app.api.root.routers import specialists

PREFIX = "/"


def create_app() -> "FastAPI":
    """Создать подприложение FastAPI."""
    app = FastAPI(docs_url=None, redoc_url=None)

    app.include_router(specialists.router)

    return app
