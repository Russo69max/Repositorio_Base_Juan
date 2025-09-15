nome= input("Qual seu nome?:")
nota1 = int(input("Qual sua primeira nota?:"))
nota2 = int(input("Qual sua segunda nota?:"))
nota3 = int(input("Qual sua terceira nota?:"))
try:
    media = (nota1 + nota2 +nota3) / 3 
    with open ("Pessoa.txt","a") as beraldo:
        beraldo.write(nome + "|" + "" f+{nota1} + "|" f+ {nota2} +"|"f+{nota3} + "|" f"media:{media: .2f} \n")
except:
    print("Voce digitou errado seu burro !!!!!!")
