# API - É um lugar para disponibilizar recursos e/oou funcionalidades
# 1-objetivo - criar uma api de disponibiliza a consulta, criação, edição e exclusão de livros
# 2-url base - localhost
# 3-Endpoints - Endereço onde o usuário deve ir para fazer determinada operação.
    # localhost/livros (GET)
    # localhost/livros (POST)
    # localhost/livros/id (GET)
    # localhost/livros/id (PUT)
    # localhost/livos/id (DELETE)
# 4-Quais recursos - livros

from flask import Flask, jsonify, request

app = Flask(__name__) # criando uma aplicação flask com o nome do arquivo atual

livros =[
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor':'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Fílosofal',
        'autor':'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'James Clear',
        'autor':'Hábitos Atómicos'
    },
]

# consultar todos
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)
# consultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
# Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
# criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)
# Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)
app.run(port=5000,host='localhost',debug=True)