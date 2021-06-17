from flask import Blueprint, request, render_template, redirect, url_for, flash
from werkzeug.urls import url_parse


from SoftLife.forms.form_contact import ContactForm
from SoftLife.forms.form_auth_user import LoginForm, RegistrationForm

from ..mail import Message, mail

bp = Blueprint('Produtos', __name__)



@bp.route('/', methods=['GET', 'POST'])
def products():
    form_contact = ContactForm()
    form_login = LoginForm()
    form_registration = RegistrationForm()
    return render_template('products.html', title='Produtos',
                            form_contact=form_contact, 
                            form_login=form_login, 
                            form_registration=form_registration)

@bp.route('/<int:id>', methods=['GET', 'POST'])
def products_id(id):
    form_contact = ContactForm()
    form_login = LoginForm()
    form_registration = RegistrationForm()
    return render_template('products_id.html', title='Produtos',
                            form_contact=form_contact, 
                            form_login=form_login, 
                            form_registration=form_registration)
