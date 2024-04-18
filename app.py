# Do módulo flask importa pra mim a classe Flask
from flask import Flask, render_template, g
import sqlite3

# Criando uma instância da classe Flask, passando "Olá" como o nome do aplicativo
app = Flask("Olá")

# Criando variável para manipular o banco de dados
DATABASE = "banco.bd"
SECRET_KEY = "1234"
app.config.from_object(__name__)

# Função para criar a conexão com o banco de dados
def conectar():
    return sqlite3.connect(DATABASE)

# Função para executar a conexão
@app.before_request
def before_request():
    g.bd = conectar()

# Função para encerrar a conexão com o banco de dados
@app.teardown_request
def teardown_request(f):
    g.bd.close()

# Define uma rota para a raiz do site, utilizando o decorador @app.route("/")
@app.route('/')
# Define uma função associada à rota raiz que retorna a mensagem "Olá mundo"

def exibir_posts():
    sql = "SELECT titulo, texto, data_criacao FROM posts ORDER BY id DESC"
    resultado = g.bd.execute(sql)

    posts = [
        {"titulo": "Os Sete Maridos de Evelyn Hugo", "texto": "Querer dar um passo maior que a perna é um sinal claro de que a pessoa não sabe o que está fazendo.", "data_criacao": "13 de junho de 2017"},
        {"titulo": "Tudo em Todo o Lugar ao Mesmo Tempo", "texto": "Cada rejeição, cada decepção trouxe você aqui. Para este momento. Não deixe que nada a distraia.", "data_criacao": "23 de junho de 2022"}
    ]

    nome_usuario = ["Raquel", "Luiza", "Pedro", "João"]
    return render_template("ola.html", nome = nome_usuario, posts = posts)
