print("\033[33m*\033[m" * 50)
print(" " * 15,  "Lojas Curso Em Video")
print("\033[33m*\033[m" * 50)


valor_produto = float(input("Informe o valor do produto:"))
print('''Formas De Pagamento:
[1] - Dinheiro \033[32m(20% DE DESCONTO!!!)\033[m
[2] - Cartão a vista \033[32m(5% DE DESCONTO!!!)\033[m
[3] - Cartão parcelado \033[33m(2x ou 10x)\033[m
[4] - Cheque \033[32m(20% DE DESCONTO!!!)\033[m''')







forma_pagamento = input("Informe a forma de pagamento:")

if forma_pagamento == "1" or forma_pagamento == "4":
    desconto = valor_produto * 0.10
    valor = valor_produto - desconto
    print(f"valor a pagar: {valor} ")


elif forma_pagamento == "2":
    formula = valor_produto * 0.05
    calculo = valor_produto - formula
    print(f"valor a pagar: {calculo}")


elif forma_pagamento == "3":
    vezes = int(input("Quantas vezes?: "))
    if vezes == 2:
        calculo = valor_produto / 2
        print(f"Sua compra será parcelada em 2x de R${calculo}")
        print(f"Sua compra de R${valor_produto} vai custar R${valor_produto} no final ")
    elif vezes >= 3:
        pagamento = valor_produto / vezes
        parcela_mensal = pagamento + (pagamento * 0.20)
        formula = (valor_produto * 0.20)
        calculo = (valor_produto + formula)
        print("Sua compra será parcelada em {}x de R${:.2f}".format(vezes, parcela_mensal))
        print(f"Sua compra de R${valor_produto} vai custar R${calculo} No final")

else:
    print("OPÇÃO INVÁLIDA DE PAGAMENTO. Tente novamente ")
