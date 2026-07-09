from backend.extensions import db

class Servico(db.Model):
    __tablename__ = 'servicos'

    id = db.Column(db.Integer,primary_key = True)
    nome_servico = db.Column(db.String(150),nullable = False)
    valor = db.Column(db.Float, nullable = False)
    id_barbeiro = db.Column(db.Integer, db.ForeignKey('barbeiros.id'),nullable = False)
