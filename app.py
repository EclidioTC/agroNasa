import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS

# Configura o Flask para procurar templates e ficheiros estáticos na pasta atual
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

# Rota universal para servir qualquer ficheiro estático, CSS, JS ou JSON da raiz
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

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