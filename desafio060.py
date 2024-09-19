
option = int(input("Digite a opção que quer usar \nWhile: 1 \nFor: 2\nopção:"))


if option == 1:
#versão while - Kauet dias
    n = int(input("Digite o número que deseja saber o fatorial:"))
    fatorial = 1
    soma = 0
    while n > 1:
        fatorial *= n
        n -= 1


    print(fatorial)



#versão if - Kauet Dias
else:
    n = int(input("Digite o número que deseja saber o fatorial: "))
    fatorial = 1
    print(f"Fatorial de {n}! = ", end="")
    for i in range (n, 0, -1):
        print(f"{i}", end="")
        print(" x " if i>1 else " = ", end="")
        fatorial *= i

    print(f"{fatorial}", end="")
