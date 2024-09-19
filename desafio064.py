soma = contador = 0

numeros = int(input("Digite um número[999 = parar]: "))

while numeros != 999:
    soma += numeros
    contador += 1
    numeros = int(input("Digite outro número:"))


print(f"A soma dos {contador} digitados é: {soma}")