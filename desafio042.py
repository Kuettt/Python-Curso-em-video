print('-='*20)
print("Analisador de Triângulos")
print('-='*20)

reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo Segmento: '))
reta3 = float(input("Terceiro Segmento: "))


if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("É possível fazer um triângulo ", end='')
    if reta1 == reta2 == reta3:
        print("EQUILATERO!")

    elif reta1 == reta2 or reta1 == reta3 or reta3 == reta2:
        print("ISOCELES!")

    elif reta1 != reta2 and reta1 != reta3 and reta3 != reta2:
        print("ESCALENO!")

else:
    print("Não é possível fazer um triângulo")


