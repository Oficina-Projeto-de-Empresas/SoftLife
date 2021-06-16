from flask import Blueprint, render_template

from SoftLife.ext.db import db
from SoftLife.forms.form_contact import ContactForm
from SoftLife.forms.form_auth_user import LoginForm, RegistrationForm

bp = Blueprint('Feed', __name__)


@bp.route('/', methods=['GET', 'POST'])
def feed():
    form_contact = ContactForm()
    form_login = LoginForm()
    form_registration = RegistrationForm()
    return render_template('feed.html', title='Feed',
                            form_contact=form_contact, 
                            form_login=form_login, 
                            form_registration=form_registration)
