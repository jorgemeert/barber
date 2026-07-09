#Importação de bibliotecas e dados.
from flask import Flask
from flask_cors import CORS
from backend.extensions import db
import os
from dotenv import load_dotenv
from backend.routes.cliente import cliente_bp
from backend.routes.barbeiro import barbeiro_bp
from backend.routes.servico import servico_bp
from backend.routes.agendamento import agendamento_bp
from backend.routes.bloqueio import bloqueio_bp


#Carregando env.
load_dotenv()

#Definição de váriavel com nome do app.
app = Flask(__name__)


#Configuração do banco de dados.
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') # lê o valorda váriavel SECRET_KEY que está .env.
database_url = os.getenv('DATABASE_URL', 'sqlite:///corteja.db')
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)
app.config['SQLALCHEMY_DATABASE_URI'] = database_url


#Inicialização do banco de dados.
db.init_app(app)


#Importação dos models, para o db precisa ver e quais tabelas ele irá criar.
from backend.models.cliente import Cliente
from backend.models.barbeiro import Barbeiro
from backend.models.servico import Servico
from backend.models.agendamento import Agendamento
from backend.models.bloqueio import Bloqueio
from backend.models.bloqueio import Bloqueio

#Dizendo para o Flask que esse grupo faz parte da aplicação;
CORS(app)
app.register_blueprint(cliente_bp)
app.register_blueprint(barbeiro_bp)
app.register_blueprint(servico_bp)
app.register_blueprint(agendamento_bp)
app.register_blueprint(bloqueio_bp)

with app.app_context(): #Garante que as tabelas existam no banco indepedente de como o servidor foi iniciado.
    db.create_all()

#Inicialização do app.
@app.route('/')
def iniciar():
    return 'Está funcionado'

# Verifica se o arquvio está sendo executado diretamente.
if __name__ == '__main__':
    with app.app_context(): # Usado pois o SQLAlhemy precisa saber qual app está sendo usado no momento.
        db.create_all() # Cria as tabelas no banco de dados.
    app.run(debug=True)   #Reinicia o servidor automaticamente quando você salva o código.
