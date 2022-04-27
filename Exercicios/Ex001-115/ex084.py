galera = []
principal = []
maior = menor = 0
while True:
    galera.append(str(input('Nome: ')).title().strip())
    galera.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = galera[1]
    else:
        if galera[1] > maior:
            maior = galera[1]
        if galera[1] < menor:
            menor = galera[1]
    principal.append(galera[:])
    galera.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(principal)} pessoas ')
print(f'O maior peso foi de {maior}. Peso de ',end=' ')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]} ',end=' ')
print()
print(f'O menor peso foi de {menor}. Peso de ',end=' ')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]} ',end=' ')
print()
