from datetime import date


'''data_calendário = datetime.now()
ano_atual = data_calendário.year

print("*" * 50)
print(" " * 15 , "Checagem de alistamento", "" * 15)
print("*" * 50)
ano = int(input("Informe seu ano de nascimento: "))


if ano < 1000:
    print("Informe uma data válida")

idade = ano_atual - ano
atraso_alistamento = idade - 18
quando_alistar = 18 - idade

if idade == 18:
    print("Hora de se alistar!!!")

elif idade > 18:
    print("Já passou da hora de se alistar!!!")
    print(f"Você devia ter se alistado em {ano_atual - atraso_alistamento}!!!")


elif idade < 18:
    print("Ainda não está na hora de se alistar!!!")
    print(f"Você deverá se apresentar em {ano_atual + quando_alistar}!!!") 
'''


atual = date.today().year
sexo = input("Digite o seu genero biológico: ")




if sexo == 'Masculino' or sexo == 'M' or sexo == 'masculino' or sexo == 'm':
    nasc = int(input("Ano de Nascimento: "))
    idade = atual - nasc
    print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}")

    if idade == 18:
        print("Você tem que se alistar IMEDIATAMENTE!")

    elif idade < 18:
        saldo = 18 - idade
        print(f'Ainda faltam {saldo} ano(s) para o alistamento ')
        ano = saldo + atual
        print(f'Seu alistamento será em {ano}')

    else:
        saldo = idade - 18
        print(f"Você deveria ter se alistado há {saldo} anos")
        ano = atual - saldo
        print(f'Seu alistamento foi em {ano}')

else:
    print("Seu alistamento não é obrigatório")















'''print("               Checagem do exército                ")
print("*" * 50)


idade = int(input("Digite sua idade: "))


calculo_menor = 18 - idade
calculo_maior = idade - 18

if idade == 18:
    print("Você deve se alistar no exercito neste exato momento")

elif idade < 18:
    print(f"Ainda não é a sua hora de se alistar no exército, faltam {calculo_menor} anos!!!")

else:
    print(f"Já passou da hora de se alistar, você está atrasado {calculo_maior} anos!!!")'''