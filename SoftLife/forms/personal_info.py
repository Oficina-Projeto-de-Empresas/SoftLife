from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class PersonalInformationForm(FlaskForm):
    name = StringField('Nome completo', validators=[DataRequired('Nome não pode ficar vazio')])
    cpf = StringField('CPF', validators=[])
    email = StringField('E-mail', validators=[DataRequired('E-mail não pode ficar vazio'), Email('Informe um email válido')])
    telephone = StringField('Telefone', validators=[])
    #password = PasswordField('Senha', validators=[DataRequired('Senha Senha pode ficar vazio')])
    #confirm_password = PasswordField('Confirmar senha', validators=[DataRequired(), EqualTo('password')])

    address = StringField('Rua', validators=[])
    number = StringField('Número', validators=[])
    neighborhood = StringField('Bairro', validators=[])
    complement = StringField('Complemento', validators=[])
    zip = StringField('CEP', validators=[])
    city = StringField('Cidade', validators=[])
    state = StringField('Estado', validators=[])
    reference_point = StringField('Ponto de referência', validators=[])

    submit = SubmitField('Atualizar')

