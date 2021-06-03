from SoftLife.ext.admin import admin as base_admin
from SoftLife.ext.auth.admin import UserAdmin
from SoftLife.ext.auth.commands import add_user, list_users
from SoftLife.ext.auth.models import User
from SoftLife.ext.db import db


def init_app(app):
    """TODO: inicializar Flask Simple Login + JWT"""

    app.cli.command()(list_users)
    app.cli.command()(add_user)

    base_admin.add_view(UserAdmin(User, db.session))