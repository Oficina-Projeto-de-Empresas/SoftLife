from flask import render_template

from .main import bp as main_bp
from .auth import bp as auth_bp
from .products import bp as products_bp
from .feed import bp as feed_bp
from SoftLife.forms.form_contact import ContactForm
from SoftLife.forms.form_auth_user import LoginForm, RegistrationForm

def init_app(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp, url_prefix='/produtos')
    app.register_blueprint(feed_bp, url_prefix='/feed')

    @app.errorhandler(404)
    def not_found(e):
        form_contact = ContactForm()
        form_login = LoginForm()
        form_registration = RegistrationForm()
        return render_template('page_404.html',
                                form_contact=form_contact, 
                                form_login=form_login, 
                                form_registration=form_registration), 404