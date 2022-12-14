from sqladmin import ModelView
from wtforms.fields import TextAreaField

from app.adapters.storage.models.offices import Office, City


class OfficeAdmin(ModelView, model=Office):
    """Филиалы в админ панели."""

    name = "Филиал"
    name_plural = "Филиалы"
    icon = "fa-solid fa-hospital"

    column_list = ("id", "city", "address")
    column_labels = {
        "id": "ID",
        "city": "Город",
        "address": "Адрес",
        "description": "Описание",
        "work_time": "Рабочее время",
        "phone": "Телефон",
        "email": "E-mail",
        "main_doctor": "Главный врач",
        "main_doctor_work_time": "Приёмные часы",
        "coor_x": "Координата X",
        "coor_y": "Координата Y",
    }


class CityAdmin(ModelView, model=City):
    """Города в админ панели."""

    name = "Город"
    name_plural = "Города"
    icon = "fa-solid fa-hospital"

    column_list = ("id", "name")
    column_labels = {
        "id": "ID",
        "name": "Название города",
        "offices": "Филиалы",
    }
