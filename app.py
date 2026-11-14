from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Rota principal (Abre diretamente o Simulador USSD)
@app.route('/')
def home():
    return render_template('smartinterface.html')

# Rota alternativa explícita para o USSD
@app.route('/ussd')
def ussd_simulator():
    return render_template('smartinterface.html')

# Rota para a interface Web / Dashboard principal
@app.route('/web')
def web_dashboard():
    return render_template('index.html')

# Endpoint para previsões e dados de satélite da NASA (aceita GET e POST)
@app.route('/previsao', methods=['GET', 'POST'])
def previsao():
    if request.method == 'POST':
        # Pega os dados enviados pela interface (se houver)
        dados = request.get_json(silent=True) or request.form.to_dict()
        
        # Aqui podes ligar a tua lógica de processamento ou modelo.py
        return jsonify({
            "status": "sucesso",
            "mensagem": "Previsão e dados de satélite processados com sucesso pelo agroNasa",
            "dados_recebidos": dados
        })
    
    # Se for GET, retorna o estado do serviço de previsão
    return jsonify({
        "status": "ativo",
        "descricao": "API de monitorização agroclimática e dados da NASA - agroNasa"
    })

if __name__ == '__main__':
    app.run(debug=True)