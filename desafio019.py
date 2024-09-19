from random import choice


aluno1 = input("Digite o primeiro aluno:")
aluno2 = input("Digite o segundo aluno: ")
aluno3 = input("Digite o terceiro aluno: ")
aluno4 = input("Digite o quarto aluno: ")

alunos = aluno1, aluno2, aluno3, aluno4

escolha = choice(alunos)
print(f"O aluno escolhido foi {escolha}")
