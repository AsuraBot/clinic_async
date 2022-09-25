from fastapi import FastAPI
from app.adapters.storage.db import engine
from sqladmin import Admin, ModelView
from app.adapters.storage.models import Specialist


def create_app() -> "FastAPI":
    """Создать приложение FastAPI."""
    app = FastAPI(title="clinic", version="0.1.0", redoc_url=None)

    admin = Admin(app, engine.get_async())

    class SpecialistAdmin(ModelView, model=Specialist):
        column_list = [
            Specialist.id,
            Specialist.name,
            Specialist.photo,
            Specialist.start_work_date,
            Specialist.description,
            Specialist.on_main,
        ]

    admin.add_view(SpecialistAdmin)

    return app
