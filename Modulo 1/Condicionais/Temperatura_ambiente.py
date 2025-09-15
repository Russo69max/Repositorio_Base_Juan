nome = input("Qual é seu nome?")
temperatura = float(input("Qual a temperatura de onde vc está?"))
if temperatura >=20 and temperatura <=40:
    print(f"{nome} onde tu está tá quente pra crl")
elif temperatura <=20 and temperatura >=5:
    print(f"{nome} ai tá frio pra crl mané")
elif temperatura <=5 and temperatura >=0:
    print(f"{nome} tá gelado pra crl mané")
else:
    print(f"{nome} tu vai morre")
