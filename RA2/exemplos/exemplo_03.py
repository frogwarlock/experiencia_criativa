#app py
from flask import Flask


#objeto python
app = Flask(__name__)
##__name__ é o nome da aplicação

@app.route('/')
def index():
    return "Conteúdo da Página Inicial!"

@app.route('/sensors')
def sensors():
    return "Listar Sensores"

@app.route('/actuators')
def actuators():
    return "Listar Atuadores"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)