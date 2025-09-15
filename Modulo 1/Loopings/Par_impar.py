repetir = 's'
while repetir != 't':
    numero_escolhido  = int(input("Digite seu numero inteiro: "))

    if numero_escolhido % 2==0:
        print(f"o numero {numero_escolhido} é par: ")
    else:
        print(f"esse numero {numero_escolhido} é impar: ")
    repetir = input("Deseja verificar outro numero? s para sim,qualquer outra tecla para sair: ")
    
