from datetime import datetime

data_atual = datetime.now()
ano_atual = data_atual.year

print("*" * 50)
print(" " * 9,"Confederação Nacional de Natação")
print("*" * 50)


ano = int(input("Insira o ano de nascimento do participante: "))

idade = ano_atual - ano

if idade <= 9:
    print("O PARTICIPANTE ESTÁ NA CATEGORIA MIRIM!!!")

elif idade <= 14:
    print("O PARTICIPANTE ESTÁ NA CATEGORIA INFANTIL!!!")

elif idade <= 19:
    print("O PARTICIPANTE ESTÁ NA CATEGORIA JUNIOR!!!")

elif idade <= 25:
    print("O PARTICIPANTE ESTÁ NA CATEGORIA SÊNIOR!!!")

else:
    print("O PARTICIPANTE ESTÁ NA CATEGORIA MASTER!!!")