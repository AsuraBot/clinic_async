from app.adapters.storage.models.analyzes import Analysis, AnalysisType
from sqladmin import ModelView
from wtforms.fields import BooleanField


class AnalysisTypeAdmin(ModelView, model=AnalysisType):
    """Типы анализов в админ панели."""

    name = "Тип анализа"
    name_plural = "Типы анализов"
    icon = "fa-solid fa-vials"

    column_list = ("id", "name", "description")
    column_labels = {
        "id": "ID",
        "name": "Название",
        "description": "Описание",
        "analyzes": "Анализы",
    }

    form_ajax_refs = {
        "analyzes": {
            "fields": ("id", "name", "preparation"),
            "order_by": "name",
        }
    }


class AnalysisAdmin(ModelView, model=Analysis):
    """Анализы в админ панели."""

    name = "Анализ"
    name_plural = "Анализы"
    icon = "fa-solid fa-vial"

    form_overrides = {"is_active": BooleanField}
    form_widget_args = {"is_active": {"class": "form-check-input"}}

    column_list = ("id", "name", "preparation", "period", "is_active")
    column_labels = {
        "id": "ID",
        "name": "Название",
        "preparation": "Хз что это",
        "period": "Время проведения",
        "is_active": "Активно",
        "analyzes_types": "Типы анализов",
    }

    form_ajax_refs = {
        "analyzes_types": {
            "fields": ("id", "name"),
            "order_by": "name",
        }
    }
