lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-==-'*15)
print(f'A lista COMPLETA é: {lista}')
print(f'A lista de PARES é: {pares}')
print(f'A lista de ÍMPARES é: {impares}')