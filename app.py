from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Jantar secreto',
        'autor': 'Raphael Montes'
    },
    {
         'id': 2,
        'titulo': 'O vilarejo',
        'autor': 'Raphael Montes'
    },
    {
         'id': 3,
        'titulo': 'Dias perfeitos',
        'autor': 'Raphael Montes'
    }
]
#ver os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)
#achar por id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    return jsonify({'erro': 'Livro não encontrado'}), 404

#editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
         if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
#criar
@app.route('/livros/<int:id>', methods=['POST'])
def incluir_novo():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


#excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir(id):
    for indice, livro in enumerate(livros):
         if livro.get('id') == id:
            del livros[indice]

            return jsonify(livros)


app.run(port=5000,host='localhost',debug=True)