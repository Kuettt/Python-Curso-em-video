import random
from time import sleep


print("\033[33m-=\033[m"*10)
print("\033[33mBem vindo ao jogo de adivinhação!!!")
print('\033[33m-=\033[m'*10)
print("\033[33mPensarei em um número de 0 a 5, adivinhe qual é!!!")

usuario = int(input('\033[33mDigite o número que acha que cairá:\033[m '))
print("\033[33mProcessando...\033[m")

sleep(3)

computador = random.randrange(0, 5)
if usuario == computador:
    print(f"\033[32mParabéns, você acertou o número!!! \nO número era: {computador}\033[m")
else:
    print(f"\033[31mTente novamente! \nO número era: {computador}\033[m")

