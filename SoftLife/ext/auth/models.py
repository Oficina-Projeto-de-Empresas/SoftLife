from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from SoftLife.ext.db import db


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100), nullable=False)
    cpf = db.Column("cpf", db.String(11), unique = True, nullable=False)
    telephone = db.Column("telephone", db.String(11))
    email = db.Column("email", db.Unicode, unique=True, nullable=False)
    password = db.Column("password", db.Unicode, nullable=False)
    admin = db.Column("admin", db.Boolean)

    def __init__(self, name, cpf, telephone, admin, email, password):
        self.name = name
        self.cpf = cpf
        self.telephone = telephone
        self.admin = admin
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def __repr__(self):
        return self.name