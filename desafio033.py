
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3  = int(input("Digite o terceiro número: "))

#Verificando o número maior
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

#Verificando o maior
maior = n1

if n2>n3 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print(f'O menor valor digitado foi {menor}')
print(f"O maior valor digitado foi {maior}")





'''if n1 > n2 > n3:
    print(f"{n1} > {n2} > {n3}")

elif n1 > n3 > n2:
    print(f"{n1} > {n3} > {n2}")

elif n2 > n3 > n1:
    print(f"{n2} > {n3} > {n1}")

elif n2 > n1 > n3:
    print(f"{n2} > {n1} > {n3}")

elif n3 > n2 > n1:
    print(f'{n3} > {n2} > {n1}')

elif n3 > n1 > n2:
    print(f'{n3} > {n1} > {n2}')
else:
    print("Algo deu errado!")'''



