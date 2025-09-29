import requests

try:
    url = "https://sp.senai.br/unidade/santanadeparnaiba/"
    resposta = requests.get(url)
    repota = (resposta.status_code)
    if repota == 200:
        print("Está tudo correto | status:",repota)
    else:
        print("Erro não encontrado | status:",repota )
except:
    print("Não funcionou ")


