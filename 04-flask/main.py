from flask import Flask
app = Flask(__name__)


@app.route('/')
def Ola_Mundo():
    return 'Olá Mundo!'

