#Importação de bibliotecas e dados.
from datetime import datetime
from flask import Blueprint, request, jsonify
from backend.extensions import db
from backend.models.agendamento import Agendamento

#Criando grupo de rotas dedicado ao bloqueio.
agendamento_bp = Blueprint('agendamento',__name__)

#Dizendo a rota dessa função, para acessar pelo front-end.
@agendamento_bp.route('/agendarHorario', methods = ['POST'])
def agendar_cliente():

    #Convertando os dados que vem em JSON do front para o dicionário de python.
    dados = request.get_json()

    #Criando um objeto com os dados recebidos.
    agendamento = Agendamento(
        dia = datetime.strptime(dados['dia'], '%d/%m/%Y').date(),
        horario = datetime.strptime(dados['horario'], '%H:%M').time(),
        id_cliente = dados['id_cliente'],
        id_barbeiro = dados['id_barbeiro'],
        id_servico = dados['id_servico']

    )

    #Verificando seu o usuário já não tem um agendamento ativo.
    agendamento_ativo = Agendamento.query.filter_by(id_cliente = dados['id_cliente']).first()

    #Caso haja um agendamento, uma mensagem de erro para o front-end.
    if agendamento_ativo:
        return jsonify({'mensagem':'Infelizmente você já tem um agendamento ativo!'}),401


    #Caso haja sucesso, manda o objeto para o banco de dados.
    db.session.add(agendamento)
    db.session.commit()

    #Mensagem de sucesso para o front-end.
    return jsonify({'mensagem':f'Seu agendamento foi concluído pra o dia {agendamento.dia} no horário {agendamento.horario}'}),200


#Dizendo a rota dessa função, para acessar pelo front-end.
@agendamento_bp.route('/mostrarAgendamentos/<int:id_barbeiro>', methods = ['GET'])
def mostrar_agendamentos(id_barbeiro):

    #Procurando os ids do barbeiro nos agendamentos.
    agendamentos = Agendamento.query.filter_by(id_barbeiro = id_barbeiro).all()

    #Caso o barbeiro não tenha nenhum agendamento.
    if not agendamentos:
        return jsonify ({'mensagem':'Você não tem nenhum agendamento!'}),404


    #Mandando para o front-end as informações dos agendamentos ativos do barbeiro.
    return jsonify([{'id':a.id,'dia': str(a.dia), 'horario': str(a.horario),'id_cliente': a.id_cliente,'id_servico': a.id_servico}for a in agendamentos]),200


#Dizendo a rota dessa função, para acessar pelo front-end.
@agendamento_bp.route('/agendamentosAtivos/<int:id_cliente>', methods = ['GET'])
def agendamentos_ativos(id_cliente):

    #Verificando se o id do cliente está salvo.
    agendamentos_cliente = Agendamento.query.filter_by(id_cliente = id_cliente).first()

    #Caso não esteja, quer dizer que o cliente não possui agendamentos.
    if not agendamentos_cliente:
        return jsonify({'mensagem':'Você não possui agendamentos!'}),404

    #Caso tenha, retorna para o front-end, os dados do agendamento.
    return jsonify({

        'dia': str(agendamentos_cliente.dia),
        'horario': str(agendamentos_cliente.horario),
        'id_barbeiro': agendamentos_cliente.id_barbeiro,
        'id_servico': agendamentos_cliente.id_servico
        }),200

#Dizendo a rota dessa função, para acessar pelo front-end.
@agendamento_bp.route('/cancelarAgendamento/<int:id>', methods = ['DELETE'])
def cancelar_agendamento(id):


    id_agendamento = Agendamento.query.filter_by(id = id).first()

    if not id_agendamento:
        return jsonify({'mensagem':'Você não possui agendamentos'}),404

    db.session.delete(id_agendamento)
    db.session.commit()

    return jsonify({'mensagem' : 'Agendamento cancelado com sucesso!'}),200
