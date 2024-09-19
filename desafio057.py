
sexo = str(input("Digite seu sexo: ")).upper().strip()[0]

while sexo not in "MmFf":
    sexo = str(input("Valor inválido, informe novamente: ")).upper().strip()[0]

print(f"Sexo {sexo} armazenado com sucesso!")
