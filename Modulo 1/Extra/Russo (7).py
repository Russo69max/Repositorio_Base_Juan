nome =  input("Qual o seu nome? ")
peso = float(input("Qual é seu peso em quilos?"))
altura = float(input("Qual a sua altura em metros?"))
Faixa = print("Menor que 18.5  Abaixo do peso \n 18.5 a 24.9   Peso normal \n 25.0 a 29.9  Sobrepeso \n 30.0 a 34.9  Obesidade Grau I \n 35.0 a 39.9  Obesidade Grau II \n 40.0 ou mais   Obesidade Grau III (mórbida)")
print("-------------------------------------------------")
imc= (peso / (altura * altura))
IMC = (peso / (altura * altura))
if IMC <= 18.5:
    print(f"{nome} voce está abaixodo peso e seu IMC é {imc}")
elif IMC <= 24.9:
    print(f"{nome} voce está com peso normal e seu IMC é {imc}")
elif IMC <= 29.9:
    print(f"{nome} voce está com sobre peso e seu IMC é {imc}")
else:
    print(f"{nome} tome cuidado seu IMC é {imc}")


    


