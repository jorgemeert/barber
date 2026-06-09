from backend.extensions import db

class Serviço(db.Model):
    __tablename__ = 'servicos'

    id = db.Column(db.Integer,primary_key = True)
    nome_servico = db.Column(db.String(150),nullable = False)
    valor = db.Column(db.Float(100),nullable = False)
    id_barbeiro = db.Column(db.Integer, db.ForeignKey('barbeiros.id'),nullable = False)
