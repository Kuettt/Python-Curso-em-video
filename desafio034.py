
salario = float(input('Digite seu salário atual: '))

aumento10 = salario + (salario * 0.10)
aumento15 = salario + (salario * 0.15)
if salario > 1250.00:
    print(f"Parabéns, graças ao seu bom desempenho, recebeu um aumento salárial \nSalário Antigo -> {salario}\nSalario Atual -> {aumento10}")

else:
    print(f"Parabéns, graças ao seu bom desempenho, recebeu um aumento salárial \nSalário Antigo -> {salario}\nSalario Atual -> {aumento15}")


