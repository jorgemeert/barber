from datetime import datetime
from flask import Blueprint, request, jsonify
from backend.extensions import db
from backend.models.agendamento import Agendamento

agendamento_bp = Blueprint('agendamento',__name__)

@agendamento_bp.route('/agendarHorario', methods = ['POST'])
def agendar_cliente():

    dados = request.get_json()

    agendamento = Agendamento(
        dia = datetime.strptime(dados['dia'], '%d/%m/%Y').date(),
        horario = datetime.strptime(dados['horario'], '%H:%M').time(),
        id_cliente = dados['id_cliente'],
        id_barbeiro = dados['id_barbeiro'],
        id_servico = dados['id_servico']

    )

    agendamento_ativo = Agendamento.query.filter_by(id_cliente = dados['id_cliente']).first()

    if agendamento_ativo:
        return jsonify({'mensagem':'Infelizmente você já tem um agendamento ativo!'}),401


    db.session.add(agendamento)
    db.session.commit()

    return jsonify({'mensagem':f'Seu agendamento foi concluído pra o dia {agendamento.dia} no horário {agendamento.horario}'})
