from werkzeug.urls import url_parse

from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user

from SoftLife.ext.db import db
from SoftLife.ext.auth import User
from SoftLife.forms.form_auth_user import LoginForm, RegistrationForm

bp = Blueprint('auth',__name__)


@bp.route('/entrar', methods=['GET', 'POST'])
def login():
    form_login = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('site.index'))
    if request.method == 'POST':
        if form_login.validate_on_submit():
            user = User.query.filter_by(email=form_login.email.data).first()
            if not user or not user.verify_password(form_login.password.data):
                flash('Invalid username or password', 'danger')
                return redirect(url_for('site.index'))        
            login_user(user)
            return redirect(url_for('site.index'))
    return render_template('login.html', title='entrar',
                            form_login=form_login)

@bp.route('/cadastrar', methods=['GET', 'POST'])
def register():
    form_registration = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('site.index'))
    if request.method == 'POST':
        if form_registration.validate_on_submit():
            user = User(name=form_registration.username.data, 
                        cpf=form_registration.cpf.data,
                        telephone=form_registration.telefone.data,
                        email=form_registration.email.data,
                        password=form_registration.password.data,
                        admin = False)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template('register.html', title='cadastrar',
                            form_registration=form_registration)

@bp.route('/sair')
def logout():
    logout_user()
    return redirect(url_for('site.index'))