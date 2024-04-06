# Do módulo flask importa pra mim a classe Flask
from flask import Flask
app = Flask(__name__)

# Criando uma instância da classe Flask, passando "Olá" como o nome do aplicativo
app = Flask("Olá")

# Define uma rota para a raiz do site, utilizando o decorador @app.route("/")
@app.route("/")

# Define uma função associada à rota raiz que retorna a mensagem "Olá mundo"
def ola():
    return "Olá mundo"