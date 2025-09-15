preço= int(input("Quanto vc quer converter, Digite o valor:"))
opçao= 2
while opçao !=3:
    opçao= int(input("Digite 1 para converter real em dolar \nDigite 2 para converter dolar em real \nDigite 3 para sair do sistema "))
    if opçao  == 1:
        print(preço * 5.80)
    elif opçao == 2:
        print(preço * 0.18)
    else:
        print("")
       

