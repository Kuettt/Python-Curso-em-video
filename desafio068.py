from random import randint

soma = contador = 0
print("=-"*30)
print("VAMOS JOGAR PAR OU IMPAR")
print("=-"*30)
while True:

    computador = randint(0, 10)
    n = int(input("Digite um número:"))
    soma = computador + n

    par_impar = str(input("Par ou Impar?[P/I]:")).strip()[0]

    while par_impar not in "PpIi":
        par_impar = str(input("Par ou Impar?[P/I]:")).strip()[0]

    if soma % 2 == 0 and par_impar in "Pp":
        print(f"Você jogou {n} e o computador jogou {computador}, Deu {soma} PAR\nVitoria do jogador")
        contador += 1
    elif soma % 2 != 0 and par_impar in "Ii":
        print(f"Você jogou {n} e o computador jogou {computador}, Deu {soma} IMPAR")
        print("Vitória do Jogador")
        contador += 1

    else:
        break

print("-"*15)
print(f"Você perdeu!!!\nVitórias do jogador:{contador}")

