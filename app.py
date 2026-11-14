from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from modelo import responder_assistente

app = Flask(__name__, static_folder='.', template_folder='.')
CORS(app)

@app.route('/')
def index():
    # Serve o novo index.html da raiz do projeto
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    # Permite ao servidor carregar CSS, JS e ficheiros de áudio da pasta audio/
    return send_from_directory('.', filename)

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    dados = request.get_json()
    pergunta = dados.get('pergunta', '')
    regiao = dados.get('regiao', 'Maputo / Boane')
    
    resposta = responder_assistente(pergunta, regiao)
    return jsonify({"resposta_assistente": resposta})

if __name__ == '__main__':
    app.run(debug=True, port=5000)