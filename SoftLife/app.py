from flask import Flask
from SoftLife.ext import config
from SoftLife.ext import db
from SoftLife.ext import auth
from SoftLife.ext import admin
from SoftLife.ext import cli
from SoftLife.ext import site
from SoftLife.ext import mail

def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    cli.init_app(app)
    auth.init_app(app)
    admin.init_app(app)
    mail.init_app(app)
    # here we invoke each extension's init_app function

    site.init_app(app)
    return app
