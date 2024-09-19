maior_mil = vezes_looping = soma_produtos = barato_preco = 0
barato_nome = "indefinido"
print("="*30)
print("LOJA SUPER BARATÃO")
print("="*30)

while True:
    vezes_looping += 1
    nome = str(input("Nome do Produto:"))
    preco = float(input("Preço: R$"))
    soma_produtos += preco

    if vezes_looping == 1:
        barato_nome = nome
        barato_preco = preco

    if preco > 1000:
        maior_mil += 1

    if preco < barato_preco:
        barato_nome = nome
        barato_preco = preco

    continuar = str(input("Quer continuar? [S/N]"))[0].strip()
    while continuar not in "SsNn":
        continuar = str(input("Quer continuar? [S/N]"))[0].strip()

    if continuar in "Nn":
        break

print("{:-^40}".format("Fim do programa"))
print(f"O total da compra foi R${soma_produtos:.2f}")
print(f"Temos {maior_mil} custando mais de R$1000.00")
print(f"O produto mais barato foi {barato_nome} que custa R${barato_preco:.2f}")
