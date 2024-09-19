while True:
    n = int(input("Quer ver a tabuada de qual valor?"))
    if n < 0:
        break
    print("-"*30)
    for i in range(1, 11):
        soma = n * i
        print(f"{n} x {i} = {soma}")
    print("-"*30)

print("Obrigado por usar nosso programa!")










