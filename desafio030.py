

print('\033[33mBem vindo ao jogo de par ou impar!!!')
print('\033[33mAqui estão as regras:\n1.Digite um número que seja maior que -1\n2.Só são aceitos números\n3.Divirta-se :)\033[m')
number = int(input('\033[33mDigite um número:\033[m'))

if number % 2 == 0:
    print("\033[32mÉ um número Par!!!")
else:
    print("\033[32mÉ um número Impar\033[m")

