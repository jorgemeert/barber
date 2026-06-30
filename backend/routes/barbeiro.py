#Importação de funções e bibliotecas
import bcrypt
from flask import Blueprint, request, jsonify
from backend.extensions import db
from backend.models.barbeiro import Barbeiro

#Criando grupo de rotas dedicado ao Barbeiro.
barbeiro_bp = Blueprint('barbeiro',__name__)

#Dizendo a rota dessa função, para acessar pelo front-end.
@barbeiro_bp.route('/cadastroBarbeiro', methods = ['POST'])
def cadastrar_barbeiro():

    #Convertando os dados que vem em JSON do front para o dicionário de python.
    dados = request.get_json()

    #Criptografando a senha do barbeiro, para uma melhor segurança.
    senha_hash = bcrypt.hashpw(dados['senha'].encode('utf-8'),bcrypt.gensalt())

    #Criando um objeto com os dados recebidos.
    novo_barbeiro = Barbeiro(
        nome = dados['nome'],
        nome_barbearia = dados['nome_barbearia'],
        senha = senha_hash,
        localizacao = dados['localizacao'],
        telefone = dados['telefone'],
        foto = dados['foto']

    )

    #Mandando o objeto criado para o banco de dados.
    db.session.add(novo_barbeiro)
    db.session.commit()

    #Retornando uma mensagem de sucesso para o front-end.
    return jsonify({'mensagem':'Barbeario cadastrada com sucesso!', 'id' : novo_barbeiro.id}),201

#Dizendo a rota dessa função, para acessar pelo front-end.
@barbeiro_bp.route('/loginBarbeiro', methods = ['POST'])
def login_barbeiro():

    #Convertando os dados que vem em JSON do front para o dicionário de python.
    dados = request.get_json()

    #Filtrando de barbeiro pelo número, para um verificação.
    barbeiro = Barbeiro.query.filter_by(telefone = dados['telefone']).first()

    #Caso não seja encontrado, quer dizer que esse barbeiro não está cadastrado, ou login incorreto.
    if barbeiro == None:
        return jsonify({'mensagem':'Barbeiro não encontrado.'}),404

    #Comparando a senha que o usário colocou com a senha criptografada do banco de dados.
    if bcrypt.checkpw(dados['senha'].encode('utf-8'),barbeiro.senha):
        #Mensagem de sucesso para o front-end.
        return jsonify({'mensagem':'Login correto! Seja bem-vindo!','id':barbeiro.id}),200

    #Caso o a senha esteja incorreta.
    else:
        return jsonify({'mensagem':'Senha incorreta!'}),400


#Dizendo a rota dessa função, para acessar pelo front-end.
@barbeiro_bp.route('/barbearias',methods = ['GET'])
def mostrar_barbearias():

    #Procurando todas as barbearias do banco de dados.
    barbeiro = Barbeiro.query.all()

    #Caso não exista barbearias cadastradas.
    if not barbeiro:
      return jsonify({'mensagem':'Nenhuma barbearia cadastrada'})

    #Retornando as Barbearias para o front-end.
    return jsonify([{'nome':b.nome, 'nome_barbearia':b.nome_barbearia,'id':b.id,'foto': b.foto, 'localizacao' : b.localizacao}for b in barbeiro])


#Dizendo a rota dessa função, para acessar pelo front-end.
@barbeiro_bp.route('/pesquisarBarbearia', methods = ['POST'])
def pesquisar_barbearia():

    #Convertando os dados que vem em JSON do front para o dicionário de python.
    dados = request.get_json()

    #Procurando as barbearias que foi recebida pelo front-end.
    barbeiro = Barbeiro.query.filter_by(nome_barbearia = dados['nome_barbearia']).first()

    #Caso não ache a barbearia.
    if barbeiro == None:
        return jsonify({'mensagem' : 'Nenhuma barbearia com esse nome foi encontrado!'})

    #Retornando os dados da barbeaira para o front-end.
    else:
        return jsonify([{'nome':barbeiro.nome, 'nome_barbearia':barbeiro.nome_barbearia,'id':barbeiro.id,'foto': barbeiro.foto, 'localizacao' : barbeiro.localizacao}])



