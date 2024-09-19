print('-='*20)
print("Analisador de Triângulos")
print('-='*20)

reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo Segmento: '))
reta3 = float(input("Terceiro Segmento: "))


if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("É possível fazer um triângulo")
else:
    print("Não é possível fazer um triângulo")




'''triangulo = False

possibilidade1 = (reta1 + reta2) > reta3
possibilidade2 = (reta1 + reta3) > reta2
possibilidade3 = (reta2 + reta1) > reta3
possibilidade4 = (reta2 + reta3) > reta1
posibillidade5 = (reta3 + reta2) > reta1
possibilidade6 = (reta3 + reta1) > reta2

if possibilidade1:
    triangulo = True

if possibilidade2:
    triangulo = True



if triangulo:
    print("É possível fazer um triângulo")
else:
    print("Não é possível fazer um triângulo")'''

