import csv

tc = int(input("Quanto voce quer gastar em caminhão: "))
rc = int(input("Qual ano voce quer comprar de caminhão: "))
opcao = 1

while opcao != 4:
    opcao = int(input("1- mostra valor dos caminhões com o preço que voce digitou \n2- mostra todos os modelos de caminhão\n3- mostrar os anos dos caminhões do ano que voce digitou\n4- Encerrar o programa\nDigite: "))

    if opcao == 1:
        teste = open("csv_.csv")
        arquivo = csv.DictReader(teste)
        for linha in arquivo:
            if int(linha['Valor']) <= tc:
                print(linha)

    elif opcao == 2:
        teste = open("csv_.csv")
        arquivo = csv.DictReader(teste)
        for linha in arquivo:
            if linha['Modelo']:
                print(linha)
        print("-----------------------------------\n")

    elif opcao == 3:
        teste = open("csv_.csv")
        arquivo = csv.DictReader(teste)
        print("Digite um valor certo")
        for linha in arquivo:
            if int(linha['Ano']) == rc:
                print(linha)
    else:
        print("Encerrando o sistema")

