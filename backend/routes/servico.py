from flask import  Blueprint, request, jsonify
from backend.extensions import db
from backend.models.servico import Serviço


servico_bp = Blueprint('servico',__name__)


@servico_bp.route('/cadastroServico', methods = ['POST'])
def cadastrar_servico():

    dados = request.get_json()

    servicos_barbeiro = Serviço(
        nome_servico = dados['nome_servico'],
        valor = dados['valor'],
        id_barbeiro = dados['id_barbeiro']
    )


    db.session.add(servicos_barbeiro)
    db.session.commit()

    return jsonify({'mensagem':'Serviço cadastrado com sucesso!'}),201

@servico_bp.route('/servicos/<int:id_barbeiro>', methods=['GET'])
def listar_servicos(id_barbeiro):


    servicos = Serviço.query.filter_by(id_barbeiro = id_barbeiro).all()

    if not servicos:
        return jsonify({'mensagem':'Esse barbeiro não cadastrou nenhum serviço!'}),404

    else:
        return jsonify([{'nome': s.nome_servico, 'valor': s.valor} for s in servicos]),200
