
value1 = int(input("Digite o primeiro número:"))
value2 = int(input("Digite o segundo número:"))
choice = 0


while choice != 5:
    print("""
        Digite qual ação deseja realizar com esses dois números!
        [1] - Somar
        [2] - Multiplicar
        [3] - Maior
        [4] - Solicitar Novos números
        [5] - Sair do Programa
    """)
    choice = int(input("Qual ação deseja tomar: "))

    if choice == 1:
        soma = value1 + value2
        print("-="*5)
        print(f"A soma desses dois números é {soma}")
    elif choice == 2:
        multi = value1 * value2
        print("-="*5)
        print(f"A multiplicação desses dois números é {multi}")
    elif choice == 3:

        if value1 == value2:
            print("-="*10)
            print("Os dois possuem o mesmo valor")
        elif value1 > value2:
            print("-="*10)
            print(f"{value1} é maior que {value2}")
        else:
            print(f"{value2} é maior que {value1}")
    elif choice == 4:
        print("Digite os novos valores que deseja: ")
        value1 = int(input("Digite o primeiro número:"))
        value2 = int(input("Digite o segundo número:"))
    elif choice == 5:
        pass
    else:
        print("!="*10)
        print("A opção informada é invalida")


print("OBRIGADO POR USAR NOSSO SOFTWARE!!!")
