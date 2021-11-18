from flask import Blueprint, request, render_template, redirect, url_for, flash
from werkzeug.urls import url_parse

from SoftLife.ext.db.models import Items
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
