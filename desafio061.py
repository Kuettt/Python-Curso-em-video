
pt = int(input("Digite o Primeiro Termo:"))
razao = int(input("A razão:"))
contador = 0
pt -= razao

print(f"Progressão Aritimética:", end=" ")
while contador < 10:
    contador += 1

    pt += razao
    print(f"{pt}", end="")
    print(" - " if contador < 10 else " ", end="")

print("FIM!!")


