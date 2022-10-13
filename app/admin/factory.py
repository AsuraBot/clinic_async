from typing import cast

from flask import Flask
from flask_admin import Admin, AdminIndexView
from sqlalchemy.orm import scoped_session, sessionmaker

from app.adapters.storage.db import engine
from app.adapters.storage.db.base_model import BaseModel
from app.adapters.storage.models import Analysis
from app.admin.views.analyzes import AnalysisView

current_session = scoped_session(sessionmaker())


def create_app() -> "Flask":
    app = Flask(__name__)

    app.config["FLASK_ADMIN_SWATCH"] = "Cosmo"
    app.secret_key = "kek"

    admin = Admin(
        app,
        base_template="layouts/base.html",
        name="Административная панель",
        index_view=AdminIndexView(name="Главная", url="/"),
        template_mode="bootstrap4",
    )

    admin.add_view(AnalysisView(Analysis, current_session, name="Анализы"))

    return cast(Flask, admin.app)


if __name__ == "__main__":
    BaseModel.metadata.bind = engine.get()

    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
