from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, template_folder='.')
CORS(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/ussd', methods=['GET', 'POST'])
def ussd_simulator():
    if request.method == 'POST':
        # Captura os dados enviados pelo simulador do frontend
        dados = request.get_json(silent=True) or request.form.to_dict()
        texto = dados.get('text', '')
        
        # Lógica dos menus USSD do agroNasa
        if texto == '' or texto == '*':
            resposta = "CON AgroNasa\n1. Alerta de Seca (Boane)\n2. Previsão Agroclimática NASA\n3. Ajuda"
        elif texto == '1':
            resposta = "CON Alerta: VERMELHO\nSECA – Boane\nProbabilidade: 84%\nCompensação: 2500 MT\n* para voltar"
        elif texto == '2':
            resposta = "CON Dados NASA:\nHumidade do Solo: Baixa\nRega Recomendada: Urgente\n* para voltar"
        elif texto == '3':
            resposta = "END Sistema agroNasa ativo.\nSuporte técnico implementado com sucesso."
        else:
            resposta = "END Opção inválida. Tente novamente."
            
        return resposta
    
    return render_template('index.html')

@app.route('/web')
def web_dashboard():
    return render_template('smartinterface.html')

@app.route('/estilo.css')
def estilo():
    return send_from_directory('.', 'estilo.css')

@app.route('/app.js')
def javascript():
    return send_from_directory('.', 'app.js')

@app.route('/previsao', methods=['GET', 'POST'])
def previsao():
    if request.method == 'POST':
        dados = request.get_json(silent=True) or request.form.to_dict()
        return jsonify({
            "status": "sucesso",
            "mensagem": "Previsão processada pelo agroNasa",
            "dados_recebidos": dados
        })
    return jsonify({"status": "ativo", "descricao": "API agroNasa"})

if __name__ == '__main__':
    app.run(debug=True)