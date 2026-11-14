from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# Configura o Flask para procurar os ficheiros HTML na pasta atual
app = Flask(__name__, template_folder='.')
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

# Endpoint para previsões e dados de satélite da NASA
@app.route('/previsao', methods=['GET', 'POST'])
def previsao():
    if request.method == 'POST':
        dados = request.get_json(silent=True) or request.form.to_dict()
        return jsonify({
            "status": "sucesso",
            "mensagem": "Previsão e dados de satélite processados com sucesso pelo agroNasa",
            "dados_recebidos": dados
        })
    
    return jsonify({
        "status": "ativo",
        "descricao": "API de monitorização agroclimática e dados da NASA - agroNasa"
    })

if __name__ == '__main__':
    app.run(debug=True)