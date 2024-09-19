

peso = float(input("Informe o seu peso (KG):"))
altura = float(input("Informe sua altura (m):"))



imc = peso / (altura ** 2)
print("O IMC dessa pessoa é de {:.1f}".format(imc))

if imc < 18.5:
    print("Abaixo do peso")

elif 18.5 <= imc <= 25:
    print("Peso Ideal")

elif 25 <= imc <= 30:
    print("Sobrepeso")

elif 30 <= imc <= 40:
    print("Obesidade")

else:
    print("OBESIDADE MÓRBIDA!!")

