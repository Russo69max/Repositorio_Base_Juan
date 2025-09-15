Nome = input("Qual seu nome? ")
opçao = 2
while opçao != 4:
    opçao = int(input("Digite um numero \n 1 Faça um pix \n 2-Mostrar extrato \n 3-Fazer deposito \n 4-Saia do sistema "))
    if opçao==1:
            nome_do_cara = input("Para quem?")
            Valor = input(f"Digite o valor para {nome_do_cara} \n ")
            print(f" {nome_do_cara} recebeu {Valor}")
    elif opçao == 2:
            print (input(f"{Nome} voce ainda n tem extrato aperte enter para fazer deposito na conta"))
            D_3 = opçao = valor = int(input(f"{Nome} quanto de deposito vc quer fazer? \n  "))
            valor_final  = input(f"{Nome} voce depositou na sua conta {valor}")
    elif opçao==3: 
            valor = int(input(f"{Nome} quanto de deposito vc quer fazer? \n  "))
            valor_final  = input(f"{Nome} voce depositou na sua conta {valor}")
    else:    
        print("reiniciando o programa do sistema do banco")
    


