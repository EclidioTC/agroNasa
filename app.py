from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__, template_folder='.')
CORS(app)

# Rota principal e rota /ussd -> Abrem o Simulador USSD (index.html)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ussd')
def ussd_simulator():
    return render_template('index.html')

# Rota /web -> Abre a Interface Gráfica / Dashboard (smartinterface.html)
@app.route('/web')
def web_dashboard():
    return render_template('smartinterface.html')

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