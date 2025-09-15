import csv 

with open("dados.csv","a", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Toyota","Supra","2002","45000"])

