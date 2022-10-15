from app.adapters.storage.models.analyzes import Analysis, AnalysisType
from sqladmin import ModelView


class AnalysisAdmin(ModelView, model=Analysis):
    """Анализы в админ панели."""

    name = "Анализ"
    name_plural = "Анализы"
    icon = "fa-solid fa-flask"

    column_list = ("id", "name", "preparation", "period", "is_active")
    column_labels = {
        "id": "ID",
        "name": "Название",
        "preparation": "Хз что это",
        "period": "Время проведения",
        "is_active": "Активно",
    }


class AnalysisTypeAdmin(ModelView, model=AnalysisType):
    """Типы анализов в админ панели."""

    name = "Тип анализа"
    name_plural = "Типы анализов"
    icon = "fa-solid fa-flask"

    column_list = ("id", "name", "description")
    column_labels = {"id": "ID", "name": "Название", "description": "Описание"}
