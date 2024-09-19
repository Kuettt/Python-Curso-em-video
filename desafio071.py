
# V1 - SEM USAR O BREAK

def v1():

    nota_cinquenta = nota_vinte = nota_dez = nota_um = 0
    cont_cinquenta = cont_vinte = cont_dez = cont_um = 0
    total = 0

    print("="*40)
    print("{:^40}".format("BANCO CEV"))
    print("="*40)
    saque = int(input("Qual valor você quer sacar? R$"))

    while nota_cinquenta < saque:
        if total+50 > saque:
            break
        nota_cinquenta += 50
        total += 50
        cont_cinquenta += 1

    while nota_vinte < saque:
        if total+20 > saque:
            break
        nota_vinte += 20
        total += 20
        cont_vinte += 1

    while nota_dez < saque:
        if total+10 > saque:
            break
        nota_dez += 10
        total += 10
        cont_dez += 1

    while nota_um < saque:
        if total+1 > saque:
            break
        elif total <= saque:
            cont_um += 1
            nota_um += 1
            total += 1

    if cont_cinquenta > 0:
        print(f"Total de {cont_cinquenta} cédulas de R$50")
    if cont_vinte > 0:
        print(f"Total de {cont_vinte} cédulas de R$20")
    if cont_dez > 0:
        print(f"Total de {cont_dez} cédulas de R$10")
    if cont_um > 0:
        print(f"Total de {cont_um} cédulas de R$1")

    print("="*40)
    print("Volte sempre ao BANCO CEV! Tenha um bom dia!")

# V2 - PÓS VÍDEO DE EXPLICAÇÃO DO GUANABARA


def v2():

    print("="*40)
    print("{:^40}".format("BANCO CEV"))
    print("="*40)
    saque = int(input("Quantos deseja sacar? R$"))
    devendo = saque
    ced = 50
    totced = 0

    while True:

        if devendo >= ced:
            devendo -= ced
            totced += 1

        else:

            print(f"Total de cédulas {totced} de R${ced}")

            if ced == 50:
                ced = 20

            if ced == 20:
                ced = 10

            if ced == 10:
                ced = 1

            if devendo == 0:
                break



v2()
# Leva em conta o V1, a segunda é mais uma cópia da lógica do professor Guanabara