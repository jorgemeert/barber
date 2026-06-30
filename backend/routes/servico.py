#Importação de bibliotecas e dados.
from flask import  Blueprint, request, jsonify
from backend.extensions import db
from backend.models.servico import Serviço

#Criando grupo de rotas dedicado ao Serviço.
servico_bp = Blueprint('servico',__name__)

#Dizendo a rota dessa função, para acessar pelo front-end.
@servico_bp.route('/cadastroServico', methods = ['POST'])
def cadastrar_servico():

    #Convertando os dados que vem em JSON do front para o dicionário de python.
    dados = request.get_json()

    #Criando um objeto com os dados recebidos.
    servicos_barbeiro = Serviço(
        nome_servico = dados['nome_servico'],
        valor = dados['valor'],
        id_barbeiro = dados['id_barbeiro']
    )

    #Mandando o objeto criado para o banco de dados.
    db.session.add(servicos_barbeiro)
    db.session.commit()

    #Retornando uma mensagem de sucesso para o front-end.
    return jsonify({'mensagem':'Serviço cadastrado com sucesso!'}),201

#Dizendo a rota dessa função, para acessar pelo front-end.
@servico_bp.route('/servicos/<int:id_barbeiro>', methods=['GET'])
def listar_servicos(id_barbeiro):

    #Filtrando os serviços do barbeiro.
    servicos = Serviço.query.filter_by(id_barbeiro = id_barbeiro).all()

    #Mensagem caso não seja encontrado nenhum serviço.
    if not servicos:
        return jsonify({'mensagem':'Esse barbeiro não cadastrou nenhum serviço!'}),404

    #Caso seja encontrado, uma mensagem com os dados para o front-end.
    else:
        return jsonify([{'nome_servico': s.nome_servico, 'valor': s.valor,'id':s.id} for s in servicos]),200
