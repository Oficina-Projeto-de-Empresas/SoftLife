from flask import Blueprint, request, render_template, redirect
from SoftLife.forms.form_contact import ContactForm 

from ..mail import Message, mail


bp = Blueprint('site', __name__)

@bp.route('/')
def index():
    form = ContactForm()
    return render_template('index.html', title='Inicial', form=form)

@bp.route('/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        send_message(request.form)
        # flash('Mensagem enviada com sucesso!!!') Renderizar na tela
        return redirect('/')    
    return render_template('index.html', form=form)

def send_message(message):
    msg = Message(message.get('subject'), sender = message.get('email'),
            recipients = ['vinicius.tertuliano@aluno.faculdadeimpacta.com.br'],
            body= message.get('message')
    )  
    mail.send(msg)