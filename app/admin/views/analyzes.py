from flask_admin.contrib.sqla import ModelView


class AnalysisView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    create_template = "models/create.html"
    list_template = "models/list.html"
    # edit_template = 'microblog_edit.html'
    # create_template = 'microblog_create.html'
    # list_template = 'microblog_list.html'
    # details_template = 'microblog_details.html'
    # edit_modal_template = 'microblog_edit_modal.html'
    # create_modal_template = 'microblog_create_modal.html'
    # details_modal_template = 'microblog_details_modal.html'
    # form_columns = ["individual", "month", "sum"]

    # column_sortable_list = ["created_at", "month"]

    # column_formatters = {"individual": individ_formatter}
