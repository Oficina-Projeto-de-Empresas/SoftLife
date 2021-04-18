from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired('Nome não pode ficar vazio')])
    email = StringField('E-mail', validators=[DataRequired('E-mail não pode ficar vazio'),Email('Informe um email válido')])
    subject = StringField('Assunto', validators=[DataRequired('Assunto não pode ficar vazio')])
    message = TextAreaField('Mensagem', validators=[DataRequired('Mensagem não pode ficar vazio')])
    submit = SubmitField("Enviar")

    def __init__(self, name_original=None, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.name_original = name_original