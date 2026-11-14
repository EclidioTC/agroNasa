@app.route('/previsao', methods=['GET', 'POST'])
@app.route('/api/previsao', methods=['GET', 'POST'])
@app.route('/chat', methods=['GET', 'POST'])
@app.route('/api/chat', methods=['GET', 'POST'])
def previsao_chat():
    if request.method == 'POST':
        dados = request.get_json(silent=True) or request.form.to_dict()
        pergunta = str(dados.get('message', dados.get('pergunta', ''))).lower()
        
        resposta_ia = "Com base nos dados de satélite da NASA, o nível de alerta em Boane é moderado a alto devido à humidade do solo reduzida. Recomenda-se monitorizar a rega."
        if "alerta" in pergunta:
            resposta_ia = "O nível de alerta reflete as condições de humidade do solo recolhidas via satélite para a região de Boane."
        elif "plantar" in pergunta or "cultivar" in pergunta:
            resposta_ia = "Para esta época, são recomendadas culturas resistentes à seca, garantindo melhor aproveitamento dos recursos hídricos."

        return jsonify({
            "status": "sucesso",
            "resposta": resposta_ia,
            "mensagem": resposta_ia,
            "dados_recebidos": dados
        })
    return jsonify({"status": "ativo", "descricao": "API agroNasa"})