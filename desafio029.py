
velocimetro = int(input("Velocidade registrada: "))


if velocimetro >= 81:
    multa =  (velocimetro - 80) * 7.00
    print(f'\033[31mMULTADO seu veículo foi visto muito acima do permitido!!!\nMulta:{multa} R$\033[m')
    print('\033[31m=\033[m' * 60)
else:
    print("\033[32mTenha um BOM DIA!!! Dirija com segurança\033[m")