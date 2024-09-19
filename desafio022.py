
nome = input("Digite um nome: ").strip()
print("Analisando seu nome...")

print(f"Nome com letras Maiúsculas: {nome.upper()}")
print(f"Nome com letras minúsculas: {nome.lower()}")

print(f"Letras ao todo: {len(nome.replace(' ', ''))}")

nome = nome.split()

print(f"O primeiro nome tem: {len(nome[0])} letras")


