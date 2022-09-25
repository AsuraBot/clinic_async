from sqladmin import Admin, ModelView
from app.adapters.storage.models import Specialist


admin = Admin()


class SpecialistAdmin(ModelView, model=Specialist):
    column_list = [Specialist.id, Specialist.name]


admin.add_view(SpecialistAdmin)
