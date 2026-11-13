from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "Sucesso",
        "mensagem": "API do agroNasa a funcionar perfeitamente!",
        "responsavel": "Membro 2 - Backend & Infraestrutura"
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)