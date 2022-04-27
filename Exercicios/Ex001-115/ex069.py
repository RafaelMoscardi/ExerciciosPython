print('-=-' * 9)
print(' CADASTRE UMA PESSOA ')
print('-=-' * 9)
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
         sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    resp = ' '
    while resp not in 'SN':
        print('-=-' * 9)
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        print('-=-' * 9)
    if resp == 'N':
        break
print('ACABOU...')