from typing import TYPE_CHECKING
from app.adapters.storage.db import engine
from sqladmin import Admin
from app.api.admin.routers.analyzes import AnalysisAdmin, AnalysisTypeAdmin

if TYPE_CHECKING:
    from fastapi import FastAPI

PREFIX = "/admin"


def create_app(app: "FastAPI") -> None:
    """Добавить роутеры админ-панели."""

    admin = Admin(app, engine.get_async(), base_url=PREFIX, title="Админ-панель")

    admin.add_view(AnalysisTypeAdmin)
    admin.add_view(AnalysisAdmin)
