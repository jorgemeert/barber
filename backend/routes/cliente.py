#Importando dados e funções de biblioteca.
import bcrypt # Bliblioteca que criptografa a senha de forma aleátoria.
from flask import Blueprint, request , jsonify
#Blueprint - Forma de organizar as rotas em grupos.
#Request - Objeto que contém os dados que o usuário enviou.
#Jsonify - Converte os dados python para JSON, para devolver ao front-end. Toda API REST responde em JSON.
from backend.extensions import db
from backend.models.cliente import Cliente

#Criação de grupo de rotas, criando uma seção da API dedicada ao cliente.
cliente_bp = Blueprint('cliente',__name__)

#Diz que quando frontend fizer uma requisição POST para /cadastro, o Flask vai executar a função cadastrar_cliente.
@cliente_bp.route('/cadastro', methods=['POST'])
#Método GET - Busca dados (GET FICA APARARENTE NA URL). POST - ENVIA DADOS PARA O SERVIDOR.
def cadastrar_cliente():
  #Transforma o dados recebidos em JSON para o dicionário Python.
  dados = request.get_json()

  #Criptografa a senha.
  senha_hash = bcrypt.hashpw(dados['senha'].encode('utf-8'),bcrypt.gensalt())
  #bcrypt.hashpw(...) - Aplica o hash de verdade.
  #dados['senha'] - Pega a senha que o usário digitou.
  #encode('utf-8') - Converte a senha de texto pra bytes.
  #bcrypt.gensalt() - Gera uma 'valor' aleátorio apartir daquela senha.

  #Salva os dados em tabela como estava la no models.
  novo_cliente = Cliente(
    nome = dados['nome'],
    telefone = dados['telefone'],
    senha = senha_hash
  )

  #Coloca o cliente em uma fila de operação pedente.
  db.session.add(novo_cliente)
  #Faz o que estava na fila ser enviado ao banco de dados.
  db.session.commit()

  #retorna para o front end uma mensagem de sucesso, devolve em JSON, pois o front só recebe e envia em JSON.
  return jsonify({'mensagem':'Cliente cadastrado com sucesso!'}),201

# 200 — sucesso
# 201 — criado com sucesso
# 400 — requisição inválida (dados errados)
# 401 — não autorizado (precisa de login)
# 404 — não encontrado
# 500 — erro interno do servidor

#Login do usuário.
@cliente_bp.route('/login', methods = ['POST'])
#Função para o login.
def login_cliente():
  #transforma os dados de JSON do front-end para a linguagem de Python.
  dados = request.get_json()

  #Verifando se o cliente já está registrado no app ( pelo telefone).
  #filtra e procura apenas o telefone e verifica se o telefone que foi preenchido é o mesmo que está no banco de dados.
  #e o .first() é pra retornar o primeiro que ele encontra, pra não precisar percorrer o banco de dados inteiro.
  cliente = Cliente.query.filter_by(telefone = dados ['telefone']).first()

  #Caso o número não bata com nenhum do banco de dados, o usuário não está registrado.
  if cliente == None:
    return jsonify({'mensagem':'Usário não encontrado.'}),404

  #verificação de senha.
  if bcrypt.checkpw(dados['senha'].encode('utf-8'),cliente.senha):
  #bcrypt.checkpw(...) - método que verifica senha.
  #cliente.senha - É o hash que está salvo no banco.
  #dados['senha'].ecode('UTF-8') - Senha que o usário digitou.
    return jsonify({'mensagem':'Login correto! Seja bem-vindo!'}),200

  else:
    return jsonify({'mensagem':'Senha incorreta!'}),400

