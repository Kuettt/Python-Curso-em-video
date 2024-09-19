
# Jeito Kauet
'''
pessoas = []
qtdeM20 = 0
homemVelho = None
for c in range(4):
    pessoa = {}
    pessoa['nome'] = str(input(f"Digite o nome da {c+1}º pessoa:"))
    pessoa['idade'] = int(input(f"Digite a idade da {c+1}º pessoa:"))
    pessoa['genero'] = str(input(f"Digite o gênero biológico da {c+1}º pessoa:"))
    pessoas.append(pessoa)


somaIdades = sum(p['idade'] for p in pessoas)
qtdePessoas = len(pessoas)
mediaPessoas = somaIdades / qtdePessoas

for p in pessoas:
    if p['genero'].lower() == 'masculino':
        maisVelho = max(pessoas, key=lambda p: p['idade'])

for p in pessoas:

    if p['genero'].lower() == 'feminino':

        if p['idade'] < 20:
            qtdeM20 += 1

print(f"A média de pessoas no grupo é: {mediaPessoas}")

for p in pessoas:
    if p['genero'].lower() == 'masculino':
        if homemVelho is None or p['idade'] > homemVelho['idade']:
            homemVelho = p

if homemVelho:
    print(f"O homem mais velho da lista é o {homemVelho['nome']} com {homemVelho['idade']} anos de idade")
else:
    print(f"Não a homens na lista")

for p in pessoas:
    if p['genero'].lower == 'feminino':
        if p['idade'] < 20:
            qtdeM20 += 1

if qtdeM20 > 0:
    print(f"E temos {qtdeM20} mulheres abaixo dos 20")
'''

# Jeito Guanabara

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'------{p} PESSOA ---------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input("Sexo [M/F]:")).strip()

    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in ('Ff') and idade < 20:
        totmulher20 += 1

    somaidade += idade

mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade}')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} com menos de 20 anos')
