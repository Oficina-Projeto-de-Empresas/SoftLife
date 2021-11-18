from werkzeug.urls import url_parse

from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user

from SoftLife.ext.db import db
from SoftLife.ext.auth import User
from SoftLife.forms.form_contact import ContactForm
from SoftLife.forms.form_auth_user import LoginForm, RegistrationForm

from ..mail import send_message

bp = Blueprint('site', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    form_contact = ContactForm()
    form_login = LoginForm()
    form_registration = RegistrationForm()
    if request.method == 'POST':
        if form_contact.validate_on_submit():
            send_message(request.form)
            flash('Mensagem enviada com sucesso!!!', 'success') 
            return redirect('/')
    return render_template('index.html', title='Inicial',
                            form_login = form_login,
                            form_registration = form_registration,
                            form_contact=form_contact)
