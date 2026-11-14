from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, template_folder='.')
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

# Rotas para servir os ficheiros estáticos e JSON diretamente
@app.route('/estilo.css')
def estilo():
    return send_from_directory('.', 'estilo.css')

@app.route('/app.js')
def javascript():
    return send_from_directory('.', 'app.js')

@app.route('/frases_validadas.json')
def frases_json():
    return send_from_directory('.', 'frases_validadas.json')

@app.route('/contrato_oficial.json')
def contrato_json():
    return send_from_directory('.', 'contrato_oficial.json')

@app.route('/previsao', methods=['GET', 'POST'])
def previsao():
    if request.method == 'POST':
        dados = request.get_json(silent=True) or request.form.to_dict()
        return jsonify({
            "status": "sucesso",
            "mensagem": "Previsão processada com sucesso pelo agroNasa",
            "dados_recebidos": dados
        })
    return jsonify({"status": "ativo", "descricao": "API agroNasa"})

if __name__ == '__main__':
    app.run(debug=True)