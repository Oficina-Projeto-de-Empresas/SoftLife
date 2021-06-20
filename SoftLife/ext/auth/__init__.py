from flask_login import LoginManager

from SoftLife.ext.admin import admin as base_admin
from SoftLife.ext.auth.admin import UserAdmin
from SoftLife.ext.auth.commands import add_user, list_users
from SoftLife.ext.auth.models import User
from SoftLife.ext.db import db


def init_app(app):
    login = LoginManager(app)
    login.login_view = 'auth.login'
    login.init_app(app)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    base_admin.add_view(UserAdmin(User, db.session))