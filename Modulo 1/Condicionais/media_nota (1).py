nome = input("Qual seu nome?")
nota = float(input("Qual é sua nota?"))
nota2 = float(input("Qual é sua nota2?"))
nota3 = float(input("Qual é sua nota3?"))
media = (nota+nota2+nota3)/3
if media >= 7:
    print(f"{nome} está nota boa")
elif media >= 5:
    print(f"{nome} está nota mediana" )
else :
    print(f"{nome } está com nota pessima seu burro")






