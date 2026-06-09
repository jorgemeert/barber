from backend.extensions import db

class Agendamento(db.Model):
    __tablename__ = 'agendamentos'
    id = db.Column(db.Integer, primary_key = True)
    dia = db.Column(db.Date,nullable = False)
    horario = db.Column(db.Time, nullable = False)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable = False )
    id_barbeiro = db.Column(db.Integer, db.ForeignKey('barbeiros.id'),nullable = False)
    id_servico = db.Column(db.Integer, db.ForeignKey('servicos.id'),nullable=False)
