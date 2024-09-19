
print("=-"*71)
print(" "*38, "SEQUENCIA DE FIBONACCI", " "*36)
print("=-"*71)


limite_sequencia = int(input("Quantos números da sequência deseja ver:"))
contador = 0
n1 = -1
n2 = 1
n3 = 0

while contador < limite_sequencia:
    contador += 1
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" - ")

print("FIM")


