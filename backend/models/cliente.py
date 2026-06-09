from backend.extensions import db

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100),nullable = False)
    telefone = db.Column(db.String(15),nullable = False)
    senha = db.Column(db.String(255),nullable = False)
