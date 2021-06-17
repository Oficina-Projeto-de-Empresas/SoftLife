from werkzeug.urls import url_parse

from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user

from SoftLife.ext.db import db
from SoftLife.ext.auth import User
from SoftLife.forms.form_contact import ContactForm
from SoftLife.forms.form_auth_user import LoginForm, RegistrationForm

from ..mail import Message, mail


bp = Blueprint('site', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    form_contact = ContactForm()
    form_login = LoginForm()
    form_registration = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('site.index'))
    if request.method == 'POST':
        if form_login.validate_on_submit():
            user = User.query.filter_by(email=form_login.email.data).first()
            if user is None or not user.check_password(form_login.password.data):
                flash('Invalid username or password', 'danger')
                return redirect(url_for('site.index'))
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('site.index')
            return redirect(next_page)
        if form_registration.validate_on_submit():
            user = User(name=form_registration.username.data, 
                        cpf=form_registration.cpf.data,
                        telephone=form_registration.telefone.data,
                        email=form_registration.email.data,
                        admin = False)
            user.set_password(form_registration.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!', 'success')
            return redirect(url_for('site.index'))
        if form_contact.validate_on_submit():
            send_message(request.form)
            flash('Mensagem enviada com sucesso!!!', 'success') 
            return redirect('/')
    return render_template('index.html', title='Inicial',
                            form_contact=form_contact, 
                            form_login=form_login, 
                            form_registration=form_registration)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

def send_message(message):
    msg = Message(message.get('subject'), sender = message.get('email'),
            recipients = ['vinicius.tertuliano@aluno.faculdadeimpacta.com.br'],
            body= message.get('message')
    )  
    mail.send(msg)