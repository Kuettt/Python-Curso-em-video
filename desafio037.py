



print("\033[32m=\033[m" * 20)
print("\033[32mConversor de números")
print("\033[32m=\033[m" * 20)
print("[1] - Binário")
print("[2] - Octal ")
print("[3] - Hexadecimal")

conversao = int(input("Digite qual o tipo de conversão: "))
numero = int(input("Agora digite qual o número que deseja converter: "))

if conversao == 1:
    calculo = bin(numero)
    print(f"O valor em binário de \033[32m{numero}\033[m é \033[32m{calculo}\033[32m!")
elif conversao == 2:
    calculo = oct(numero)
    print(f"O valor em octal de \033[32m{numero}\033[m é \033[32m{calculo}\033[32m!")

elif conversao == 3:
    calculo = hex(numero)
    print(f"O valor em hexadecimal de \033[32m{numero}\033[m é \033[32m{calculo}\033[32m!")

#METODO GUANABARA



#num = int(input('Digite um número inteiro : '))
#print('''Escolha uma das bases para a conversão:
#[ 1 ] converter para BINÁRIO
#[ 2 ] converter para OCTAL
#[ 3 ] converter para HEXADECIMAL''')
#opção = int(input("Sua opção: "))

#if opção == 1:
#    print(f"{num}`convertido para BINÁRIO é igual a {bin(num)[2:]}")
#elif opção == 2:
#    print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")
#elif opção == 3:
#    print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
#else:
#    print("Opção inválida, tente novamente.")