from datetime import datetime
from flask import Blueprint, request, render_template, redirect, url_for, flash
from SoftLife.ext.db import db
from SoftLife.ext.db.models import Address, Items, OrderItems, Order
from SoftLife.forms.form_contact import ContactForm

from ..mail import send_message

bp = Blueprint('Produtos', __name__)

@bp.route('/', methods=['GET', 'POST'])
def products():
    form_contact = ContactForm()
    products = Items.query.all()
    if request.method == 'POST':
        if form_contact.validate_on_submit():
            send_message(request.form)
            flash('Mensagem enviada com sucesso!!!', 'success')
            return redirect(url_for('Produtos.products'))
    return render_template('products.html', title='Produtos', products=products,
                            form_contact=form_contact)

@bp.route('/<int:id>', methods=['GET', 'POST'])
def products_id(id):
    form_contact = ContactForm()
    product = Items.query.get(id)
    if request.method == 'POST':
        if form_contact.validate_on_submit():
            send_message(request.form)
            flash('Mensagem enviada com sucesso!!!', 'success')
            return redirect(url_for(f'Produtos.products_id({id})'))
    return render_template('products_id.html', title='Produtos', product=product,
                            form_contact=form_contact)

@bp.route('/add-cart/<int:id>?<int:user_id>', methods=['GET', 'POST'])
def add_cart(id, user_id):
    if bool(Order.query.filter(Order.completed == False).first()) is True:
        order = Order.query.filter(Order.completed == False).first()
        order_items = OrderItems.query.filter(OrderItems.order_id == order.id).all()
        for order_item in order_items:
            print(order_item.items_id)
            if order_item.items_id == id:
                db.session.query(OrderItems).filter(OrderItems.items_id == id and OrderItems.order_id == order.id)\
                        .update({"quant": order_item.quant + 1})
                db.session.commit()
                return redirect(url_for('Produtos.products'))
        order_items = OrderItems(order_id=order.id,
                            items_id=id,
                            quant=1)
        db.session.add(order_items)
        db.session.commit()
        return redirect(url_for('Produtos.products'))

    else:
        address = Address.query.filter(Address.user_id == user_id).first()
        if address == None:
            flash('Endereço não cadastrado!!!', 'danger')
            return redirect(url_for('Produtos.products'))
        else:
            order = Order(created_at=datetime.now(),
                        completed=False,
                        user_id=user_id,
                        address_id=address.id)
            db.session.add(order)
            db.session.commit()
            order = Order.query.filter(Order.completed == False).first()
            order_items = OrderItems(order_id=order.id,
                                    items_id=id,
                                    quant=1)
            db.session.add(order_items)
            db.session.commit()
    return redirect(url_for('Produtos.products'))
    