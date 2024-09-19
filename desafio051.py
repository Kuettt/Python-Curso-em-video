
primeiroTermo = int(input("Digite o primeiro termo:"))
razao = int(input("Digite a razão:"))
decimoTermo = primeiroTermo + (10-1) * razao

for c in range(primeiroTermo, decimoTermo + razao, razao):
    print(c)