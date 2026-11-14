# 🛰️ agroNasa

> Sistema de monitorização agroclimática e alerta precoce baseado em dados de satélite da NASA, combinando acessibilidade móvel (via simulador USSD) e uma interface web interativa.

[![Status do Deploy](https://img.shields.io/badge/Render-Live-success?style=flat-square&logo=render)](https://agronasa.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)

---

##  Sobre o Projeto

O **agroNasa** é uma solução tecnológica desenvolvida para apoiar o setor agrícola (com foco em pequenos agricultores e gestores agrícolas em Moçambique). O projeto integra dados climáticos e de satélite da NASA para fornecer diagnósticos de risco agrícola (como prevenção de secas), combinando duas vertentes de acesso:
1. **Canal USSD:** Simulação de interface de telemóvel de baixo custo para acesso rápido por parte de agricultores sem smartphones ou com acesso limitado à internet.
2. **Painel Web (Dashboard):** Interface gráfica completa para monitorização agroclimática detalhada.

---

##  Acesso Online (Live Demo)

A aplicação encontra-se totalmente operacional e hospedada na nuvem:
* **🌐 Link Principal / Simulador USSD:** [https://agronasa.onrender.com](https://agronasa.onrender.com)[cite: 10]
* **📱 Rota USSD Explícita:** [https://agronasa.onrender.com/ussd](https://agronasa.onrender.com/ussd)
* **💻 Painel Web / Dashboard:** [https://agronasa.onrender.com/web](https://agronasa.onrender.com/web)

---

##  Funcionalidades Principais

* **Simulador USSD Interativo:** Permite navegar por menus em formato de telemóvel para consulta rápida de alertas e condições climáticas.
* **Painel Web de Monitorização:** Visualização de dados agroclimáticos avançados e estados de cultivo.
* **API de Previsão Climática:** Endpoints configurados em Flask para processamento de dados e integração com fontes de satélite da NASA.

---

##  Tecnologias Utilizadas

O projeto foi desenvolvido utilizando a seguinte pilha tecnológica:

* **Backend:** Python, Flask, Flask-CORS, Gunicorn
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
* **Controlo de Versões:** Git & GitHub
* **Deploy & Hospedagem:** Render (Cloud Platform)

---

##  Estrutura de Rotas da Aplicação

| Rota | Descrição |
| :--- | :--- |
| `GET /` | Página principal (Simulador USSD) |
| `GET /ussd` | Acesso direto ao simulador USSD |
| `GET /web` | Interface gráfica / Dashboard web |
| `GET/POST /previsao` | Endpoint de API para dados e previsões de satélite |

---

##  Como Executar o Projeto Localmente

Se quiseres executar e testar o projeto na tua máquina local, segue estes passos:

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/EclidioTC/agronasa.git](https://github.com/EclidioTC/agronasa.git)
   cd agronasa