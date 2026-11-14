import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS

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
@app.route('/chat', methods=['GET', 'POST'])
@app.route('/api/chat', methods=['GET', 'POST'])
@app.route('/api/chatbot', methods=['GET', 'POST'])
def previsao_chat():
    if request.method == 'POST':
        dados = request.get_json(silent=True) or request.form.to_dict()
        pergunta = str(dados.get('message', dados.get('pergunta', ''))).lower()
        regiao = dados.get('regiao', 'Boane (Maputo)')
        
        resposta_ia = f"Com base nos dados de satélite da NASA para {regiao}, o nível de alerta é moderado a alto devido à humidade do solo reduzida. Recomenda-se monitorizar a rega."
        if "alerta" in pergunta:
            resposta_ia = f"O nível de alerta para {regiao} reflete as condições de humidade do solo recolhidas via satélite."
        elif "plantar" in pergunta or "cultivar" in pergunta:
            resposta_ia = "Para esta época, são recomendadas culturas resistentes à seca, como mandioca e batata-doce, garantindo melhor aproveitamento dos recursos hídricos."

        return jsonify({
            "status": "sucesso",
            "nivel_risco": "Moderado a Alto",
            "confianca": "89%",
            "cultivadas": "Milho, Feijão, hortícolas",
            "recomendadas": "Mandioca, Batata-doce, sorgo",
            "evitar": "Culturas de ciclo curto com alta exigência hídrica sem rega garantida",
            "seguro_parametrizado": "1.500 MZN",
            "resposta_assistente": resposta_ia,
            "resposta": resposta_ia,
            "mensagem": resposta_ia,
            "dados_recebidos": dados
        })
    return jsonify({"status": "ativo", "descricao": "API agroNasa"})

if __name__ == '__main__':
    app.run(debug=True)