import os
import os.path as op
import locale

from flask import Markup, url_for
from flask_admin import Admin, form
from flask_admin.contrib.sqla import ModelView

from SoftLife.ext.db import db
from SoftLife.ext.db.models import Category, Items, Address, Checkout, Order, OrderItems

file_path = op.join(op.dirname(__file__), '../static/img/products') # path
try:
    os.mkdir(file_path)
except OSError:
    pass


admin = Admin()


def init_app(app):
    admin.name = app.config.get("ADMIN_NAME", "Softlife")
    admin.template_mode = app.config.get("ADMIN_TEMPLATE_MODE", "bootstrap4")
    admin.init_app(app)

    admin.add_view(ModelView(Address, db.session))

    admin.add_view(ItemsAdmin(Items, db.session))

    admin.add_view(ModelView(Category, db.session))

    admin.add_view(ModelView(OrderItems, db.session))
    
    admin.add_view(ModelView(Order, db.session))
    
    admin.add_view(ModelView(Checkout, db.session))

class ItemsAdmin(ModelView):

    def format_price(self, request, items, *args):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        price = locale.currency(items.price, grouping=True, symbol=None)
        return f'R$ {price}'
    
    def _list_thumbnail(view, context, model, name):
        if not model.image:
            return ''

        return Markup(
            '<img src="%s">' %
            url_for('static',
                    filename=form.thumbgen_filename(model.image))
        )

    column_formatters = {
        "price": format_price,
        "image": _list_thumbnail
    }

    form_extra_fields = {
        "image": form.ImageUploadField(
            'Image', base_path=file_path, thumbnail_size=(100, 100, True))
    }
