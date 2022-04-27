print('=-=' * 12)
print('        BEM VINDO AO BANCO MOSCARDI        ')
print('=-=' * 12)
v = int(input('Que valor você quer sacar? R$'))
t = v
ced = 50
totced = 0
while True:
    if t >= ced:
        t -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if t == 0:
            break
print('=-=' * 12)
print('    Volte sempre ao BANCO MOSCARDI!    ')
print('=-=' * 12)