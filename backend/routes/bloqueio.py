from datetime import datetime
from flask import Blueprint, request, jsonify
from backend.extensions import db
from backend.models.bloqueio import Bloqueio

bloqueio_bp = Blueprint('bloqueio',__name__)

@bloqueio_bp.route('/bloquarDia', methods = ['POST'])
def bloquear():

    dados = request.get_json()
    verifica = Bloqueio.query.filter_by(data=datetime.strptime(dados['data'], '%d/%m/%Y').date(),id_barbeiro = dados['id_barbeiro']).first()

    if verifica:
        return jsonify({'mensagem':'Digite dados válidos!'})

    bloqueio_barbeiro = Bloqueio(
        data = datetime.strptime(dados['data'], '%d/%m/%Y').date(),
        horario = datetime.strptime(dados['horario'], '%H:%M').time(),
        id_barbeiro = dados['id_barbeiro']
    )

    db.session.add(bloqueio_barbeiro)
    db.session.commit()

    return jsonify({'mensagem':'Dia , horário bloqueado com sucesso!'})
