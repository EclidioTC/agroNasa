import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
from modelo import prever_risco_agricola, responder_assistente

app = Flask(__name__, template_folder='.', static_folder='.')
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ussd')
def ussd_simulator():
    return render_template('index.html')

@app.route('/web')
def web_dashboard():
    return render_template('smartinterface.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

@app.route('/previsao', methods=['GET', 'POST'])
@app.route('/api/previsao', methods=['GET', 'POST'])
def previsao_api():
    if request.method == 'POST':
        dados = request.get_json(silent=True) or request.form.to_dict()
        regiao = dados.get('regiao', 'Boane')
        data_str = dados.get('data', datetime.now().strftime("%Y-%m-%d"))
        simulacao = dados.get('simulacao', 'verde')

        # Utiliza o modelo.py para obter os dados científicos consistentes
        resultado = prever_risco_agricola(regiao, data_str)
        
        # Se for simulação específica, ajusta o dicionário conforme a escolha do utilizador
        if simulacao == 'amarelo':
            resultado.update({"nivel": "amarelo", "cenario": "Chuva Irregular", "probabilidade": 0.76, "compensacao": 1800})
        elif simulacao in ['seca', 'cheia']:
            resultado.update({"nivel": "vermelho", "cenario": "Seca Severa / Risco de Cheia", "probabilidade": 0.89, "compensacao": 4500})
        else:
            resultado.setdefault("probabilidade", 0.92)

        return jsonify({
            "status": "sucesso",
            "regiao": resultado.get("regiao", regiao),
            "nivel": resultado.get("nivel", "verde"),
            "cenario": resultado.get("cenario", "Humidade Ideal"),
            "probabilidade": resultado.get("probabilidade", 0.92),
            "culturas_recomendadas": resultado.get("culturas_recomendadas", ["Milho", "Feijão"]),
            "culturas_a_evitar": resultado.get("culturas_a_evitar", []),
            "compensacao": resultado.get("compensacao", 0),
            "explicacao": f"Dados de satélite NASA MODIS validados para {regiao}.",
            "fonte": "NASA Space Apps / MODIS"
        })
    return jsonify({"status": "ativo", "descricao": "API agroNasa Previsão"})

@app.route('/chat', methods=['GET', 'POST'])
@app.route('/api/chat', methods=['GET', 'POST'])
@app.route('/api/chatbot', methods=['GET', 'POST'])
def chatbot_api():
    if request.method == 'POST':
        dados = request.get_json(silent=True) or request.form.to_dict()
        pergunta = str(dados.get('mensagem', dados.get('pergunta', ''))).lower()
        regiao = dados.get('regiao', 'Boane')
        
        # Utiliza o modelo.py para gerar a resposta inteligente do assistente
        resposta_ia = responder_assistente(pergunta, regiao)

        return jsonify({
            "status": "sucesso",
            "resposta_assistente": resposta_ia,
            "resposta": resposta_ia,
            "mensagem": resposta_ia
        })
    return jsonify({"status": "ativo", "descricao": "API agroNasa Chatbot"})

if __name__ == '__main__':
    app.run(debug=True)