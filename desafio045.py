from random import choice, randint
from time import sleep
'''print("\033[33m*\033[m" * 50,)
print(" " * 17, "\033[33;1mJoken-po Game\033[m")
print("\033[33m*\033[m" * 50)

movimento_usuario = input("Digite seu movimento:").lower()

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)
movimentos_jokenpo = ("pedra", "papel", "tesoura")

jokenpo = choice(movimentos_jokenpo)


if movimento_usuario == jokenpo:
    print(f"EMPATE!!!\nMovimento do Player: {movimento_usuario}\nMovimento do Computador: {jokenpo}")

# Derrota usuário
elif jokenpo == 'pedra' and movimento_usuario == 'tesoura':
    print("Derrota!!!")
    print(f"Movimento do Computador: {jokenpo}")
    print(f"Movimento do Player: {movimento_usuario}")

elif jokenpo == 'tesoura' and movimento_usuario == 'papel':
    print("Derrota!!!")
    print(f"Movimento do Computador: {jokenpo}")
    print(f"Movimento do Player: {movimento_usuario}")

elif jokenpo == "papel" and movimento_usuario == 'pedra':
    print("Derrota!!!")
    print(f"Movimento do Computador: {jokenpo}")
    print(f"Movimento do Player: {movimento_usuario}")

# Vitória usuário
elif jokenpo == 'pedra' and movimento_usuario == 'papel':
    print("VITÓRIA!!!")
    print(f"Movimento do computador: {jokenpo}")
    print(f"Movimento do Player: {movimento_usuario}")

elif jokenpo == 'tesoura' and movimento_usuario == 'pedra':
    print("Vitória!!!")
    print(f"Movimento do computador: {jokenpo}")
    print(f"Movimento do Player: {movimento_usuario}")

elif jokenpo == 'papel' and movimento_usuario == 'tesoura':
    print("Vitória!!!")
    print(f"Movimento do Computador: {jokenpo}")
    print(f"Movimento do usuário :{movimento_usuario}")'''

# Método Guanabara

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
[0] - Pedra
[1] - Papel
[2] - Tesoura''')

jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)

if computador == 0: # Computador Jogou pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VITÓRIA DO JOGADOR!')
    elif jogador == 2:
        print('VITÓRIA DO COMPUTADOR!')

    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1: # Computador jogou Papel
    if jogador == 0:
        print("VITÓRIA DO COMPUTADOR!")

    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VITÓRIA DO JOGADOR!')
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('VITÓRIA DO JOGADOR!')

    elif jogador == 1:
        print('VITÓRIA DO COMPUTADOR!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print("JOGADA INVÁLIDA!")




