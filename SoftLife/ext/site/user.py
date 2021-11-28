from flask import Blueprint, render_template, redirect, url_for, request, flash
from SoftLife.ext.db import db
from SoftLife.ext.auth import User
from SoftLife.ext.db.models import Address
from SoftLife.forms.form_contact import ContactForm
from SoftLife.forms.personal_info import PersonalInformationForm

from ..mail import send_message

bp = Blueprint('usuario', __name__)

@bp.route('/<int:id>/informacoes-pessoais', methods=['GET', 'POST'])
def personal_info(id):
    form_contact, form_persona_information = ContactForm(), PersonalInformationForm()
    user = User.query.get(id)
    address = Address.query.filter(Address.user_id == user.id).first()
    if request.method == 'POST':
        if form_contact.validate_on_submit():
                send_message(request.form)
                flash('Mensagem enviada com sucesso!!!', 'success')
                return redirect(url_for('usuario.personal_info', id = user.id))
        elif form_persona_information.validate_on_submit():
            if bool(Address.query.filter(Address.user_id == user.id).first()) is True:
                print("Entrou")
                db.session.query(Address).filter(Address.id == address.id)\
                        .update({"address": form_persona_information.address.data,
                                "number":form_persona_information.number.data,
                                "neighborhood":form_persona_information.neighborhood.data,
                                "complement":form_persona_information.complement.data,
                                "zip":form_persona_information.zip.data,
                                "city":form_persona_information.city.data,
                                "state":form_persona_information.state.data,
                                "reference_point":form_persona_information.reference_point.data,
                                })
                db.session.commit()
                db.session.query(User).filter(User.id == user.id)\
                    .update({"name":form_persona_information.name.data,
                            "cpf":form_persona_information.cpf.data,
                            "email":form_persona_information.email.data,
                            "telephone":form_persona_information.telephone.data})
                db.session.commit()
                print('commit colunas')
                flash('Alteração salva com sucesso!!!', 'success')
                return redirect(url_for('usuario.personal_info', id = user.id))
            else:
                address = Address(address=form_persona_information.address.data,
                                number=form_persona_information.number.data,
                                neighborhood=form_persona_information.neighborhood.data,
                                complement=form_persona_information.complement.data,
                                zip=form_persona_information.zip.data,
                                city=form_persona_information.city.data,
                                state=form_persona_information.state.data,
                                reference_point=form_persona_information.reference_point.data,
                                user_id=user.id)
                db.session.query(User).filter(User.id == user.id)\
                    .update({"name":form_persona_information.name.data,
                            "cpf":form_persona_information.cpf.data,
                            "email":form_persona_information.email.data,
                            "telephone":form_persona_information.telephone.data})
                db.session.add(address)
                print('add colunas')
                db.session.commit()
                print('commit colunas')
                flash('Alteração salva com sucesso!!!', 'success')
                return redirect(url_for('usuario.personal_info', id = user.id))
    elif request.method == 'GET':
        if bool(Address.query.filter(Address.user_id == user.id).first()) is False:
            address  = Address(address=" ",
                            number=" ",
                            neighborhood=" ",
                            complement=" ",
                            zip=" ",
                            city=" ",
                            state=" ",
                            reference_point=" ")
        form_persona_information.name.data=user.name
        form_persona_information.cpf.data=user.cpf
        form_persona_information.email.data=user.email
        form_persona_information.telephone.data=user.telephone

        form_persona_information.address.data=address.address
        form_persona_information.number.data=address.number
        form_persona_information.neighborhood.data=address.neighborhood
        form_persona_information.complement.data=address.complement
        form_persona_information.zip.data=address.zip
        form_persona_information.city.data=address.city
        form_persona_information.state.data=address.state
        form_persona_information.reference_point.data=address.reference_point
    return render_template('personal_info.html', title='Informacoes pessoais',
                            form_persona_information=form_persona_information,
                            form_contact=form_contact)

@bp.route('/<int:id>/pedidos', methods=['GET'])
def pedidos(id):
    return 'Tela pedidos'