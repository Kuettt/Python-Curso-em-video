from datetime import date

cont_minor = 0
cont_older = 0
ano_atual = date.today().year

for c in range(0, 7):
    n = int(input(f"Digite o ano de nascimento da {c+1} pessoa:"))
    idade = (ano_atual - n)
    if idade < 21:
        cont_minor += 1
    else:
        cont_older += 1


print(f"Das 7 pessoas temos \n{cont_minor} menores de idade \n{cont_older} maiores de idade")
