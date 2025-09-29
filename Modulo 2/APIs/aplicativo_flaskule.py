from flask import Flask 
def start():
    nome = input("Qual seu nome?:")
    idade = int(input("Qual sua idade?:"))
    numero1 = int(input("Escolha um numero para calcular soma,divisão,multiplicação,subtração:"))
    numero2 = int(input("Escolha um numero para calcular soma,divisão,multiplicação,subtração:"))
    app = Flask(__name__)

    @app.route('/') #criar rotas
    def home():
        return '<h1>Hello Flask<h1>'#valor apresentado 
    @app.route('/login')
    def login():
        return (f"Seja bem vindo {nome},{idade} ao sistema")

    @app.route('/soma')
    def soma():
        return (f"soma dos numeros requisitados:{numero1+numero2}")

    @app.route('/subtração')
    def subtração():
        return (f"subtração dos numeros requisitados:{numero1-numero2}")

    @app.route('/divisão')
    def divisão():
        return (f"divisão dos numeros requisitados:{numero1/numero2}")

    @app.route('/multiplicação')
    def multiplicação():
        return (f"multiplicação dos numeros requisitados:{numero1*numero2}")
    if __name__=="__main__":
        app.run(debug=True)

start()
