#Importação de funções e bibliotecas
import bcrypt# Bliblioteca que criptografa a senha de forma aleátoria.
from flask import Blueprint, request, jsonify
#Blueprint - Forma de organizar as rotas em grupos.
#Request - Objeto que contém os dados que o usuário enviou.
#Jsonify - Converte os dados python para JSON, para devolver ao front-end. Toda API REST responde em JSON.
from backend.extensions import db
from backend.models.barbeiro import Barbeiro

barbeiro_bp = Blueprint('barbeiro',__name__)

@barbeiro_bp.route('/cadastroBarbeiro', methods = ['POST'])
def cadastrar_barbeiro():

    dados = request.get_json()

    senha_hash = bcrypt.hashpw(dados['senha'].encode('utf-8'),bcrypt.gensalt())

    novo_barbeiro = Barbeiro(
        nome = dados['nome'],
        nome_barbearia = dados['nome_barbearia'],
        senha = senha_hash,
        localizacao = dados['localizacao'],
        telefone = dados['telefone'],
        foto = dados['foto']

    )

    db.session.add(novo_barbeiro)
    db.session.commit()

    return jsonify({'mensagem':'Barbeario cadastrada com sucesso!'}),201


@barbeiro_bp.route('/loginBarbeiro', methods = ['POST'])
def login_barbeiro():

    dados = request.get_json()

    barbeiro = Barbeiro.query.filter_by(telefone = dados['telefone']).first()

    if barbeiro == None:
        return jsonify({'mensagem':'Barbeiro não encontrado.'}),404


    if bcrypt.checkpw(dados['senha'].encode('utf-8'),barbeiro.senha):
        return jsonify({'mensagem':'Login correto! Seja bem-vindo!'}),200

    else:
        return jsonify({'mensagem':'Senha incorreta!'}),400


@barbeiro_bp.route('/barbearias',methods = ['GET'])
def mostrar_barbearias():

    barbeiro = Barbeiro.query.all()

    if not barbeiro:
      return jsonify({'mensagem':'Nenhuma barbearia cadastrada'})


    return jsonify([{'nome':b.nome, 'nome_barbearia':b.nome_barbearia,'id':b.id,'foto': b.foto, 'localizacao' : b.localizacao}for b in barbeiro])


@barbeiro_bp.route('/pesquisarBarbearia', methods = ['POST'])
def pesquisar_barbearia():

    dados = request.get_json()

    barbeiro = Barbeiro.query.filter_by(nome_barbearia = dados['nome_barbearia']).first()

    if barbeiro == None:
        return jsonify({'mensagem' : 'Nenhuma barbearia com esse nome foi encontrado!'})

    else:
        return jsonify([{'nome':barbeiro.nome, 'nome_barbearia':barbeiro.nome_barbearia,'id':barbeiro.id,'foto': barbeiro.foto, 'localizacao' : barbeiro.localizacao}])



