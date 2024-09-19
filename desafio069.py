
maior_dezoito = homens = mulheres_menos_vinte = 0

while True:
    print("-"*20)
    print("CADASTRE UMA PESSOA")
    print("-"*20)
    idade = int(input("Idade:"))
    sexo = str(input("Sexo: [M/F] "))[0].strip()
    while sexo not in "FfMm":
        sexo = str(input("Sexo: [M/F] "))[0].strip()

    if idade >= 18:
        maior_dezoito += 1
    if sexo in "Mm":
        homens += 1
    if sexo in "Ff" and idade < 20:
        mulheres_menos_vinte += 1

    continuar = str(input("Deseja continuar: [S/N] "))[0].strip()

    while continuar not in "SsNn":
        continuar = str(input("Deseja continuar: [S/N] "))[0].strip()

    if continuar in "Nn":
        break


print("="*5, "FIM DO PROGRAMA", "="*5)
print(f"Total de pessoas com mais de 18 anos: {maior_dezoito}")
print(f"Ao todo temos {homens} homens cadastrados")
print(f"E temos {mulheres_menos_vinte} mulheres com menos de 20 anos")