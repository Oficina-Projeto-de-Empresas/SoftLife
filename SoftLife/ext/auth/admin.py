
from flask import Markup, flash
from flask_admin.actions import action
from flask_admin.contrib.sqla import ModelView, filters

from SoftLife.ext.auth.models import User
from SoftLife.ext.db import db


class UserAdmin(ModelView):

    column_list = ('name', 'cpf', 'telephone', 'email')

    column_searchable_list = ["email"]

    column_filters = [
        "email",
        "admin",
        filters.FilterLike(
            User.email, "dominio", options=(("gmail", "Gmail"), ("uol", "Uol"))
        ),
    ]

    can_edit = False
    can_create = True
    can_delete = True

    @action("toggle_admin", "Toggle admin status", "Are you sure?")
    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids))
        for user in users.all():
            user.admin = not user.admin
        db.session.commit()
        flash(f"{users.count()} usuários alterados com sucesso!", "success")

    @action("send_email", "Send email to all users", "Are you sure?")
    def send_email(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        # 1) redirect para um form para escrever a mensagem do email
        # 2) enviar o email
        flash(f"{len(users)} emails enviados.", "success")