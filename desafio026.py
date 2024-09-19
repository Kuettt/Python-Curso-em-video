

print('=' * 20)
print("\033[32mContador de letras A\033[m")
print('=' * 20)

frase = str(input("Digite uma frase: ")).upper().strip()

print(f"\033[33mA sua frase tem:\033[m \033[32m{frase.count('A')} \033[m \033[33mA\033[m")
print(f"\033[33mAparece primeiro no indice\033[m \033[32m{frase.find('A')+1} \033[m")
print(f"\033[33mE aparece por ultimo em\033[m \033[32m{frase.rfind('A')+1}\033[m")
9