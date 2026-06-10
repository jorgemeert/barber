#Importação de bibliotecas e dados.
from flask import Flask
from backend.extensions import db
import os
from dotenv import load_dotenv
from backend.routes.cliente import cliente_bp 
 

#Carregando env.
load_dotenv()

#Definição de váriavel com nome do app.
app = Flask(__name__)


#Configuração do banco de dados.
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') # lê o valorda váriavel SECRET_KEY que está .env.
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') # É o endereço do banco de dados.


#Inicialização do banco de dados.
db.init_app(app)


#Importação dos models, para o db precisa ver e quais tabelas ele irá criar.
from backend.models.cliente import Cliente
from backend.models.barbeiro import Barbeiro
from backend.models.servico import Serviço
from backend.models.agendamento import Agendamento
from backend.models.bloqueio import Bloqueio

#Dizendo para o Flask que esse grupo faz parte da aplicação;
app.register_blueprint(cliente_bp)

#Inicialização do app.
@app.route('/')
def iniciar():
    return 'Está funcionado'

# Verifica se o arquvio está sendo executado diretamente.
if __name__ == '__main__':
    with app.app_context(): # Usado pois o SQLAlhemy precisa saber qual app está sendo usado no momento.
        db.create_all() # Criaas tabelas no banco de dados.
    app.run(debug=True)   #Reinicia o servidor automaticamente quando você salva o código.
