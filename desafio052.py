
num = int(input("Digite o número: "))
tot = 0

for c in range(1, num+1):

    if num % c == 0:
        print(f"{c}", end=' ')
        tot += 1

if tot > 2:
    print(f"\nO número {num} não é primo, pois ele é divisível pelos números acima")
else:
    print(f"\nO número {num} é primo, pois é divisível apenas por ele mesmo e por um")

