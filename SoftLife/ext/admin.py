from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from SoftLife.ext.db import db
from SoftLife.ext.db.models import Category, Items, Address, Checkout, Order

admin = Admin()


def init_app(app):
    admin.name = app.config.get("ADMIN_NAME", "Softlife")
    admin.template_mode = app.config.get("ADMIN_TEMPLATE_MODE", "bootstrap4")
    admin.init_app(app)

    # TODO: Proteger com senha
    # TODO: traduzir para PTBR

    admin.add_view(ModelView(Address, db.session))

    admin.add_view(ModelView(Items, db.session))

    admin.add_view(ModelView(Category, db.session))

    admin.add_view(ModelView(Order, db.session))
    
    admin.add_view(ModelView(Checkout, db.session))
