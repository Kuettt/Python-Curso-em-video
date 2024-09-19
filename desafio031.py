
distancia = float(input("Distância percorrida: "))


'''if distancia <= 200:
    calculo = distancia * 0.50
    print('Preço: {:.2f} R$'.format(calculo))

else:
    calculo = distancia * 0.45
    print('Preço: {}{:.2f}{} R$'.format(\033[32m,calculo,\033[m))'''

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print(f"Sua viagem será de \033[32m{distancia}KM!\033[m")
print(f"Preço Total: \033[32m{preco}R$\033[m")
