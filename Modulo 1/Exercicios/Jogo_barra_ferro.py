def bater_no_ezequiel_com_uma_pedaço_de_ferro ():
    print("--------------------------------------------------------------------")
    print("Voce quer bater no Ezequiel com um pedaço de ferro?")
    print("------------------------------------------------------------------------")
    opçao1 = int(input("Digite 1-Para sim \n--------------------------------------------------------------------\n2-Pular pra proxima pergunta\n--------------------------------------------------------------------\n3- Parar o sistema:\n--------------------------------------------------------------------\nDigite:"))
    if opçao1 == 1:
        print("--------------------------------------------------------------------")
        print("voce fez ele quebrar um osso")
        print("------------------------------------------------------------------------")
    elif opçao1 ==2:
        print("--------------------------------------------------------------------")
        print("bater com uma ripa de madeira no ezequiel" )
        print("------------------------------------------------------------------------")
    else:
        print("--------------------------------------------------------------------")
        print("saindo do sistema" )
    opçao2 = int(input("\n2-Pular pra proxima pergunta\n--------------------------------------------------------------------\n3- Parar o sistema:\n--------------------------------------------------------------------\nDigite:"))
    if opçao2 == 1:
        print("--------------------------------------------------------------------")
        print("Ezequiel ficou com um hematoma")
        print("------------------------------------------------------------------------")
    elif opçao2 ==2:
        print("--------------------------------------------------------------------")
        print ("Voce quer dar uma coronhada em Ezequiel ? ")
        print("------------------------------------------------------------------------")
    else:
        print("--------------------------------------------------------------------")
        print("saindo do sistema" )
    opçao3 = int(input("Digite 1-Para sim \n--------------------------------------------------------------------\n2-Pular pra proxima pergunta\n--------------------------------------------------------------------\n3- Parar o sistema:\n--------------------------------------------------------------------\nDigite:"))
    if opçao3 == 1:
        print("--------------------------------------------------------------------")
        print("Voce fez ele desmaia")
        print("------------------------------------------------------------------------")
    else:
        print("saindo do sistema" )
def fazer_pergunta ():
    pergunta = input("Voce quer sequestra o ezequiel para usar ele?")
    opçao = int(input("Digite 1- Para sequestra ele e usar ele\n--------------------------------------------------------------------\n2- para na sequestra mais tacar ele em uma lata de lixo\n--------------------------------------------------------------------\n3- Parar o sistema\n--------------------------------------------------------------------\nDigite:"))
    if opçao == 1:
        print("Voce faz ele de puta em seu cativeiro?")
        print("------------------------------------------------------------------------")
    elif opçao == 2:
        print("Ele fica mofando na lata de lixo")
        print("------------------------------------------------------------------------")
    else:
        print("saindo do sistema" )

bater_no_ezequiel_com_uma_pedaço_de_ferro()
fazer_pergunta ()

