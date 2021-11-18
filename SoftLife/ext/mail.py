from flask_mail import  Mail, Message

mail = Mail()

def init_app(app):
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'groupsoft.ti@gmail.com'
    app.config['MAIL_PASSWORD'] = 'Softlife01'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail.init_app(app)

def send_message(message):
    msg = Message(message.get('subject'), sender=message.get('email'),
            recipients = ['vinicius.tertuliano@aluno.faculdadeimpacta.com.br'],
            html = f"""<h1>Contato de novo cliente</h1>
                    <h3>Assunto: {message.get('subject')} </h3>
                    <h3>Email: {message.get('email')} </h3>
                    <h3>Nome: {message.get('name')} </h3>
                    <p style="font-weight: 600; font-size: 1em;">Mensagem: {message.get('message')}</p>
                    """)
    mail.send(msg)
