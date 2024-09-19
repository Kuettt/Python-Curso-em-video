
casa = float(input("Informe o valor da casa: "))
salario = float(input("Informe o salário do cliente: "))
anos = float(input("Em quantos anos ele pagará a casa: "))


''''''#a prestação que sai a casa
prestacao = casa / (anos * 12)

porcentagem = (prestacao / salario) * 100




if porcentagem <= 30:
    print("É possível financiar a casa\nValor das prestações: {:.2f}R$".format(prestacao))

else:
    print("É impossível financiar a casa, pois a prestação seria {:.2f}R$, que é mais de 30% do salário".format(prestacao))

