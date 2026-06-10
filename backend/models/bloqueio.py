from backend.extensions import db

class Bloqueio(db.Model):
    __tablename__ = 'bloqueio'

    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.Date, nullable = False)
    horario = db.Column(db.Time,nullable = True)
    id_barbeiro = db.Column(db.Integer, db.ForeignKey('barbeiros.id'),nullable = False)
