arsenal = []
opçao =0
while opçao !=5:
    opçao = int(input("Digite oq vc quer colocar no arsenal pra matar o ezequiel:\n1-Ver arsenal\n--------------------------------------\n2-Adicionar item no arsenal\n-----------------------------------\n3-Remover itens da mochila\n--------------------------------\n----------------------------------\n4-Modificar\n----------------------\n5-Limpar o arsenal\n6-Sair do 'jogo'\n"))
    if opçao ==1:
        print(f"itens no arsenal: \n {arsenal}")
    elif opçao ==2:
        itens = input("Digite o que vc quer colocar no arsenal 🗡️: \n ")
        arsenal.append(itens)
    elif opçao ==3:
        item = input("Digite o que voce quer tira do arsenal: \n ")
        arsenal.remove(itens)
    elif opçao == 4:
        dc = input("Digite que item voce quer modificar do arsenal 🗡️: \n")
        arsenal.index(itens)
    elif opçao == 5:
        print("limpando os itens do arsenal")
        arsenal.clear(itens)
    else:
        print("")
