

#number = input("Digite um número de 0 a 9999: ")


#try:
#    print(f"Unidade: {number[3]}\nDezena: {number[2]}\nCentena: {number[1]}\nMilhar: {number[0]}")

#except:
#    print(IndexError("Não foram inseridos 4 numeros!!!"))


# Guanabara
num = int(input('Digite um número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Analisando número {num}...')

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

