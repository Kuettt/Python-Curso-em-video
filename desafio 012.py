value = float(input("Qual o preço do produto?: "))
desconto = (value * 0.05)
desconto2 = value - desconto
print("O seu produto custa {} \nmas voce ganhou 5% de desconto e agora vale {:.2f}".format(value, desconto2))
