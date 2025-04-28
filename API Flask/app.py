from flask import Flask, jsonify, request

app = Flask(__name__)

filmes = [
    {'id': 1, 'título': 'Covil de Ladrões', 'autor': 'Christian Gudegast'},
    {'id': 2, 'título': 'A Lenda do Tesouro Perdido', 'autor': 'Jon Turteltaub'},
    {'id': 3, 'título': 'Bastardos Inglórios', 'autor': 'Quentin Tarantino'},
]

@app.route('/filmes', methods=['GET'])
def obter_filmes():
    return jsonify(filmes), 200

@app.route('/filmes/<int:id>', methods=['GET'])
def obter_filme_por_id(id):
    for filme in filmes:
        if filme.get('id') == id:
            return jsonify(filme), 200
    return jsonify({'error': 'Filme não encontrado'}), 404

@app.route('/filmes/<int:id>', methods=['PUT'])
def editar_filme_por_id(id):
    filme_alterado = request.get_json()
    for indice, filme in enumerate(filmes):
        if filme.get('id') == id:
            filmes[indice].update(filme_alterado)
            return jsonify(filmes[indice]), 200
    return jsonify({'error': 'Filme não encontrado'}), 404

@app.route('/filmes', methods=['POST'])
def incluir_novo_filme():
    novo_filme = request.get_json()
    if 'id' not in novo_filme or 'título' not in novo_filme or 'autor' not in novo_filme:
        return jsonify({'error': 'Dados incompletos'}), 400
    
    for filme in filmes:
        if filme.get('id') == novo_filme['id']:
            return jsonify({'error': 'ID já existe'}), 400

    filmes.append(novo_filme)
    return jsonify(novo_filme), 201

@app.route('/filmes/<int:id>', methods=['DELETE'])
def excluir_filme(id):
    for indice, filme in enumerate(filmes):
        if filme.get('id') == id:
            del filmes[indice]
            return jsonify({'message': 'Filme excluído com sucesso'}), 200
    return jsonify({'error': 'Filme não encontrado'}), 404

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)

