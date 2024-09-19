

soma = maior = menor = numero = int(input("Digite um número:"))
continuar = input("quer continuar[s/n]").strip()[0]
quantidade = 1

while continuar in "Ss":

    if numero != 0:
        quantidade += 1

    numero = int(input("Digite um número:"))
    soma += numero
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

    continuar = str(input("Deseja continuar o algoritmo:")).strip()[0]


media = soma / quantidade

print("A MEDIA DOS {} = {:.2f}".format(quantidade, media))
print(f"MAIOR = {maior}")
print(f"MENOR = {menor}")
print(f"ACABOU!!!")
