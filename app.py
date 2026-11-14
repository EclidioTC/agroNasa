from flask import Flask, jsonify, request
from flask_cors import CORS
from modelo import prever_risco_agricola, responder_assistente

app = Flask(__name__)
CORS(app)

@app.route('/api/dados', methods=['POST'])
def receber_dados():
    conteudo = request.get_json() or {}
    regiao = conteudo.get("regiao", "Maputo / Boane")
    data = conteudo.get("data", "2026-11-14")
    resultado = prever_risco_agricola(regiao, data)
    return jsonify({"status": "Sucesso", "resultado": resultado}), 201

# Rota do Assistente Inteligente do agroNasa
@app.route('/api/chatbot', methods=['POST'])
def endpoint_chatbot():
    conteudo = request.get_json() or {}
    pergunta = conteudo.get("pergunta", "")
    regiao = conteudo.get("regiao", "Maputo / Boane")
    
    # Gera a resposta com base estrita nos dados reais de satélite da NASA
    resposta_texto = responder_assistente(pergunta, regiao)
    
    return jsonify({
        "status": "Sucesso",
        "pergunta_utilizador": pergunta,
        "resposta_assistente": resposta_texto
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)