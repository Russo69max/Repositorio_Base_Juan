nome = int(input("Me fala um numero qualquer vc vc queira irmao?"))
nome2 = int(input("Onde voce quer começar?"))
nome3 = int(input("Onde vc quer terminar?"))

for i in range(nome2,nome3+1):
    print(f"{i} x {nome} = {i * nome}")

