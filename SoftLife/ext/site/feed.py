from flask import Blueprint, render_template, redirect, url_for, request, flash

from SoftLife.ext.db import db
from SoftLife.forms.form_contact import ContactForm
from SoftLife.forms.form_auth_user import LoginForm, RegistrationForm

from ..mail import send_message

bp = Blueprint('Feed', __name__)

@bp.route('/', methods=['GET', 'POST'])
def feed():
    form_contact = ContactForm()
    if request.method == 'POST':
        if form_contact.validate_on_submit():
            send_message(request.form)
            flash('Mensagem enviada com sucesso!!!', 'success')
            return redirect(url_for('Feed.feed'))
    return render_template('feed.html', title='Feed',
                            form_contact=form_contact)
