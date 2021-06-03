from SoftLife.ext.db import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100), nullable=False)
    cpf = db.Column("cpf", db.String(11), unique = True, nullable=False)
    telephone = db.Column("telephone", db.String(11))
    email = db.Column("email", db.Unicode, unique=True, nullable=False)
    passwd = db.Column("passwd", db.Unicode, nullable=False)
    admin = db.Column("admin", db.Boolean)

    def __repr__(self):
        return self.email