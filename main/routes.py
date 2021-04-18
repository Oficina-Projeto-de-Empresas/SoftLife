from flask import render_template, request, redirect, flash
from flask_mail import Mail, Message
from main.form_contact import ContactForm
from app import app
from main import bp

mail = Mail()
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'suelitertu@gmail.com'
app.config['MAIL_PASSWORD'] = 'cecilia0505'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail.init_app(app)

@bp.route('/')
def index():
    form = ContactForm()
    return render_template('index.html', title='Inicial', form=form)

@bp.route('/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        send_message(request.form)
        flash('Mensagem enviada com sucesso!!!') #Renderizar na tela
        return redirect('/')    
    return render_template('index.html', form=form)

def send_message(message):

    msg = Message(message.get('subject'), sender = message.get('email'),
            recipients = ['vinicius.tertuliano@aluno.faculdadeimpacta.com.br'],
            body= message.get('message')
    )  
    mail.send(msg)
    
