nome =  input("Qual o seu nome? ")
peso = float(input("Qual é seu peso em quilos?"))
altura = float(input("Qual a sua altura?"))

IMC = peso / (altura * altura)
if peso <= 18.5:
    print(f"{nome} vc é um Frango")
elif IMC <= 24.9:
    print(f"{nome} Está com peso normal")
elif IMC <= 29.9:
    print(f"{nome} Está com Sobre peso")
elif IMC <= 34.9:
    print(f"{nome} Está com obesidade Grau1!")
elif IMC <= 39.9:
    print(f"{nome} Está com obesidade Grau2!")
else:
    print(f"{nome} Para de comer doritos")





