from typing import TYPE_CHECKING

from sqladmin import Admin

from app.adapters.storage.db import engine
from app.api.admin.routers.analyzes import AnalysisAdmin, AnalysisTypeAdmin
from app.api.admin.routers.specialists import SpecialistAdmin, SpecializationAdmin
from app.api.admin.routers.services import ServiceTypeAdmin, ServiceAdmin

if TYPE_CHECKING:
    from fastapi import FastAPI

PREFIX = "/admin"


def create_app(app: "FastAPI") -> None:
    """Добавить роутеры админ-панели."""

    admin = Admin(app, engine.get_async(), base_url=PREFIX, title="Админ-панель")

    admin.add_view(AnalysisTypeAdmin)
    admin.add_view(AnalysisAdmin)
    admin.add_view(SpecializationAdmin)
    admin.add_view(SpecialistAdmin)
    admin.add_view(ServiceTypeAdmin)
    admin.add_view(ServiceAdmin)
