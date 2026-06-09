from backend.extensions import db

class Barbeiro(db.Model):
    __tablename__ = 'barbeiros'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100),nullable = False)
    nome_barbearia = db.Column(db.String(50),nullable = False)
    senha = db.Column(db.String(255),nullable = False)
    localizacao = db.Column(db.String(200),nullable = False)
    telefone = db.Column(db.String(15),nullable = False)
    foto = db.Column(db.String(255),nullable = False)
