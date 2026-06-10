#Importando dados e funções de biblioteca.

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
#Método GET - Busca dados. POST - ENVIA DADOS PARA O SERVIDOR.
def cadastrar_cliente():
  #Transforma o dados recebidos em JSON para o dicionário Python.
  dados = request.get_json()
  
  #Salva os dados em tabela como estava la no models.
  novo_cliente = Cliente(
    nome = dados['nome'],
    telefone = dados['telefone'],
    senha = dados ['senha']
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