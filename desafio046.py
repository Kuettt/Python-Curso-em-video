from time import sleep
from emoji import emojize
print('\033[32m-=\033[m' * 20)
print('\033[32m-=Contagem regressiva para o ano novo-=\033[m')
print('\033[32m-=\033[m' * 20)

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emojize(":fireworks: \033[32mFELIZ ANO NOVO!\033[m :fireworks:"))