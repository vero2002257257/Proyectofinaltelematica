#Este código lo puedes utilizar si deseas
#1.Llamar las librerias
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Bienvenido!'
