print("-+"*30)
print("SOMADOR DE NÚMEROS")
print("-+"*30)
soma = valores = 0

while True:
    n = int(input("Digite um número (999 para parar) :"))
    if n == 999:
        break
    soma += n
    valores += 1

print(f"A soma dos números {valores} foi {soma}!")
