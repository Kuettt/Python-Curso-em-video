import random

lotery_number = random.randrange(1, 11)
user_number = 0
many_times = 0

while user_number != lotery_number:
    user_number = int(input("Digite o número da loteria:"))

    if user_number != lotery_number:
        print(f"Infelizmente você ERROU o número era {lotery_number} TENTE NOVAMENTE !")
        many_times += 1

if many_times < 1:
    print(f"Uau você acertou de primeira\nNúmero da loteria:{lotery_number}\nSeu número:{user_number}")
    print("PARABÉNS SUA SORTE TA EM DIA!!! ")
else:
    print(f"Depois da {many_times+1} tentativas você ACERTOU!!!\n"
          f"Número da loteria:{lotery_number}\n"
          f"Seu número:{user_number}")
    print("PARABÉNS!!!!")
