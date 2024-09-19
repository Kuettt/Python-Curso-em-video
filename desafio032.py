from datetime import date


"Método Kauet (gambiarra skdskdskd)"
ano = int(input("Digite um ano: "))
if ano == 0:
   ano = date.today().year

'''
print("Verificando.")

if ano % 4 == 0:
    print('Verificando..')
    if ano % 100 == 0:
        print("Verificando...")
        if ano % 400 == 0:
            print('Ano bissexto')
        else:
            print("Não é um ano bissexto")
    else:
        print("Ano Bissexto")

else:
    print("Não é um ano Bissexto")'''

"Método Professor Guanabara"

if ano % 4 == 0 and ano % 100 != 1 or ano % 400 == 0:
    print(f"O ano \033[32m{ano}\033[m é um ano BISSEXTO")
else:
    print(f"O ano \033[32m{ano}\033[m não é um ano BISSEXTO")
