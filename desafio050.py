
soma = 0

for numero in range(1, 7):
    n = int(input(f"Digite o {numero}° número:"))
    if n % 2 == 0:
        soma += n

print(soma)
