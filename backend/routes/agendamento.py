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

    return jsonify({'mensagem':f'Seu agendamento foi concluído pra o dia {agendamento.dia} no horário {agendamento.horario}'}),200


@agendamento_bp.route('/mostrarAgendamentos/<int:id_barbeiro>', methods = ['GET'])
def mostrar_agendamentos(id_barbeiro):

    agendamentos = Agendamento.query.filter_by(id_barbeiro = id_barbeiro).all()

    if not agendamentos:
        return jsonify ({'mensagem':'Você não tem nenhum agendamento!'}),404


    return jsonify([{'dia': str(a.dia), 'horario': str(a.horario),'id_cliente': a.id_cliente,'id_servico': a.id_servico}for a in agendamentos]),200

@agendamento_bp.route('/agendamentosAtivos/<int:id_cliente>', methods = ['GET'])
def agendamentos_ativos(id_cliente):

    agendamentos_cliente = Agendamento.query.filter_by(id_cliente = id_cliente).first()

    if not agendamentos_cliente:
        return jsonify({'mensagem':'Você não possui agendamentos!'}),404

    return jsonify({
        'dia': str(agendamentos_cliente.dia),
        'horario': str(agendamentos_cliente.horario),
        'id_barbeiro': agendamentos_cliente.id_barbeiro,
        'id_servico': agendamentos_cliente.id_servico
        }),200


@agendamento_bp.route('/cancelarAgendamento/<int:id>', methods = ['DELETE'])
def cancelar_agendamento(id):

    id_agendamento = Agendamento.query.filter_by(id = id).first()

    if not id_agendamento:
        return jsonify({'mensagem':'Você não possui agendamentos'}),404

    db.session.delete(id_agendamento)
    db.session.commit()

    return jsonify({'mensagem' : 'Agendamento cancelado com sucesso!'}),200
