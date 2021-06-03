from flask_mail import  Mail, Message

mail = Mail()

def init_app(app):
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'suelitertu@gmail.com'
    app.config['MAIL_PASSWORD'] = 'cecilia0505'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail.init_app(app)
