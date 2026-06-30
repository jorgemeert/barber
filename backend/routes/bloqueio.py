#Importação de bibliotecas e dados.
from datetime import datetime
from flask import Blueprint, request, jsonify
from backend.extensions import db
from backend.models.bloqueio import Bloqueio

#Criando grupo de rotas dedicado ao bloqueio.
bloqueio_bp = Blueprint('bloqueio',__name__)


#Dizendo a rota dessa função, para acessar pelo front-end.
@bloqueio_bp.route('/bloquarDia', methods = ['POST'])
def bloquear():

    #Convertando os dados que vem em JSON do front para o dicionário de python.
    dados = request.get_json()
    #verifica se o dia já não está bloqueado.
    verifica = Bloqueio.query.filter_by(data=datetime.strptime(dados['data'], '%d/%m/%Y').date(),id_barbeiro = dados['id_barbeiro']).first()

    #Se o dia estiver bloqueado ele manda uma mensagem para o front-end.
    if verifica:
        return jsonify({'mensagem':'Esse dia já está bloqueado!'})

    #if para dar a possibilidade ao usuário deixar o horário em branco, bloqueando o dia inteiro.
    if dados['horario']:
        horario = datetime.strptime(dados['horario'], '%H:%M').time()

    #Caso o horaio esteja vazio.
    else:
        horario = None

    #Criando um objeto com os dados recebidos.
    bloqueio_barbeiro = Bloqueio(
        data = datetime.strptime(dados['data'], '%d/%m/%Y').date(),
        horario = horario,
        id_barbeiro = dados['id_barbeiro']
    )
    #Mandando o objeto criado para o banco de dados.
    db.session.add(bloqueio_barbeiro)
    db.session.commit()

    #Retornando uma mensagem de sucesso para o front-end.
    return jsonify({'mensagem':'Dia , horário bloqueado com sucesso!'})
