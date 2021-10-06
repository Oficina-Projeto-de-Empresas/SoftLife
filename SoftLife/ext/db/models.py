# -*- encoding: utf-8 -*-

from sqlalchemy import text
from SoftLife.ext.db import db


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode, unique=True)

    def __repr__(self):
        return self.name


class Items(db.Model):
    __tablename__ = "items"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode, nullable=False)
    price = db.Column("price", db.Numeric, nullable=False)
    quantity = db.Column("quantity", db.Integer, nullable=False, server_default=text("0"))
    description = db.Column("description", db.String(200), nullable=False)
    image = db.Column("image", db.Unicode, nullable=False)
    available = db.Column("available", db.Boolean)
    category_id = db.Column("category_id", db.Integer, db.ForeignKey("category.id"))

    category = db.relationship("Category", foreign_keys=category_id)

'''    def __repr__(self):
        return '<Items %r>' % (self.id)'''


class Order(db.Model):
    __tablename__ = "order"
    id = db.Column("id", db.Integer, primary_key=True)
    created_at = db.Column("created_at", db.DateTime)
    completed = db.Column("completed", db.Boolean)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
    address_id = db.Column("address_id", db.Integer, db.ForeignKey("address.id"))

    user = db.relationship("User", foreign_keys=user_id)
    address = db.relationship("Address", foreign_keys=address_id)


class OrderItems(db.Model):
    __tablename__ = "order_items"
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("order.id"))
    items_id = db.Column("items_id", db.Integer, db.ForeignKey("items.id"))
    quant = db.Column("quant", db.Integer)
    id = db.Column("id", db.Integer, primary_key=True)

    order = db.relationship("Order", foreign_keys=order_id)
    items = db.relationship("Items", foreign_keys=items_id)


class Checkout(db.Model):
    __tablename__ = "checkout"
    id = db.Column("id", db.Integer, primary_key=True)
    payment = db.Column("payment", db.Unicode)
    total = db.Column("total", db.Numeric)
    created_at = db.Column("created_at", db.DateTime)
    completed = db.Column("completed", db.Boolean)
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("order.id"))

    order = db.relationship("Order", foreign_keys=order_id)


class Address(db.Model):
    __tablename__ = "address"
    id = db.Column("id", db.Integer, primary_key=True)
    zip = db.Column("zip", db.Unicode)
    country = db.Column("country", db.Unicode)
    address = db.Column("address", db.Unicode)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))

    user = db.relationship("User", foreign_keys=user_id)