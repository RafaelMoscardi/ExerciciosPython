num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
    else:
        print('Valor duplicado, erro ao adicionar.')
    print('Valor computado...')
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break
print('=-' * 30)
num.sort()
print(f'Você adicionou os valores: {num}')