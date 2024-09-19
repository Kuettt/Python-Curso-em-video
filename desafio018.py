from math import sin, cos, tan, pi

angulo = float(input("Informe o angulo que você deseja: "))


seno = sin((pi * angulo) / 180)

cos = cos((pi * angulo) / 180)

tan = tan((pi * angulo) / 180)


print("O seno de {:.2f} é: {:.2f}\nO Cosseno de {:.2f} é: {:.2f}\nA Tangente de {:.2f} é: {:.2f}".format(angulo, seno, angulo, cos, angulo, tan))