from random import shuffle

aluno1 =  input("insira o aluno um: ")
aluno2 = input("Insira o aluno dois: ")
aluno3 = input("Insira o aluno três ")
aluno4 = input("Insira o aluno quatro ")

lista = [aluno1, aluno2, aluno3, aluno4]

shuffle(lista)

print(f"A ordem escolhida foi {lista}")

