nome = input("Qual seu nome?")
opçao = 2
while opçao !=4:
    opçao = int(input(" 1-cadastra  \n  2- fazer login  \n 4-Sair do sistema "))
    if opçao==1:
        senha = int(input(f"{nome} Qual senha voce quer colocar?"))
        nome_cadastro = input(f"{nome} Qual nome de cadastro voce quer colocar ")
    elif opçao == 2:
        senha_digitada = input(f"{nome}Digita senha ")
        nome_digitado =  input(f"{nome}Digite nome")
        print("Logado com sucesso")
        if nome_cadastro == nome_digitado and senha == senha_digitada:
            print("Logado com sucesso")
    else:
        print ("Usuario incorreto ")
    
else:
        print (f"{nome} Saindo do sistema ")   
