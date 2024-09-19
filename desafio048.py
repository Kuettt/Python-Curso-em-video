

soma = 0
count = 0
for c in range(1, 501, 2):

    if c % 3 == 0:
        count += 1
        soma += c


print(f"Dos 500 números impáres {count} são múltiplos de 3")
print(f"E a soma deles é {soma}")


