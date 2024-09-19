
pt = int(input("Digite o Primeiro Termo:"))
razao = int(input("A razão:"))
contador = 10
pt -= razao

print(f"Progressão Aritimética:")
while contador > 0:
    contador -= 1

    pt += razao
    print(f"{pt}", end=" - ")


    if contador < 1:
        print("PAUSA")
        continuar = int(input("\nDigite o próximo termo:"))
        contador = continuar




print("FIM!!")

