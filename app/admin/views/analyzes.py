from flask_admin.contrib.sqla import ModelView


class AnalysisView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    # form_columns = ["individual", "month", "sum"]

    # column_sortable_list = ["created_at", "month"]

    # column_formatters = {"individual": individ_formatter}
