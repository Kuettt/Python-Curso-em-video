
# Jeito do Kauet
"""weigths = []

for c in range(5):
    quest = float(input(f"Digite o peso da {c+1} pessoa: "))
    weigths.append(quest)

print(f'O menor peso é {min(weigths)} e o maior peso é {max(weigths)}')
"""

# Jeito Guanabara
maior = 0
menor = 0

for pessoa in range(1, 6):
    peso = float(input(f"Pessoa da {pessoa} pessoa:"))
    # Essa parte do código obviamente define ambos os valores com
    if pessoa == 1:
        maior = peso
        menor = peso
    # Essa parte do código o tempo todo compara os valores recebidos
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso


print(f"O maior peso é {maior}\nE o menor peso é {menor}")