

'''print("\033[31m*\033[m" * 50)
print("\033[31m***\033[m     \033[33mBem vindo a checagem de números!!!\033[m\033[31m     ***\033[m")
print("\033[31m*\033[m" * 50)


numero1 = int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:"))

if numero1 > numero2:
    print(f"O PRIMEIRO valor é maior")

elif numero2 > numero1:
    print(f"O SEGUNDO valor é maior")

elif numero1 == numero2:
    print("Os números tem o MESMO valor")'''


# Método Guanabara


n1 = int(input('Primeiro número:'))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print("O primeiro número é maior")
elif n1 == n2:
    print("Os numeros são IGUAIS")
else:
    print('O segundo número é maior')