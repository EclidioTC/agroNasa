from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Ativa o CORS para permitir ligações do frontend

# Rota principal
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "mensagem": "API do agroNasa a funcionar perfeitamente!",
        "responsavel": "Membro 2 - Backend & Infraestrutura",
        "status": "Sucesso"
    })

# Nova rota para receber dados agrícolas (ex: sensores ou formulários)
@app.route('/api/dados', methods=['POST'])
def receber_dados():
    conteudo = request.get_json()
    return jsonify({
        "status": "Dados recebidos com sucesso!",
        "dados": conteudo
    }), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)