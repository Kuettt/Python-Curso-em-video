
'''print("*" * 50)
print('Checagem de média')
print("*" * 50)



nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2


if media < 5.0:
    print("Reprovado")

elif 5.0 <= media <= 6.9:
    print("Recuperação")

elif media >= 7.0:
    print("APROVADO") '''


# Método Guanabara


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

média = (nota1 + nota2) / 2

print("Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}".format(nota1, nota2, média))
if 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO')
elif média < 5:
    print("O aluno está reprovado")
else:
    print("O aluno está aprovado")

