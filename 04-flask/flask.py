from flask import Flask

app = Flask(__name__)

@app.rout('/')
def Ola_Mundo():
    return 'Olá Mundo!'