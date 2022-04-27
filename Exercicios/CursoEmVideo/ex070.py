print('=='*10)
print(' LOJAS MOSCARDINERSONS ')
print('=='*10)
total = totmil = menor = cont = 0
barato = ' '
while True:
    n = str(input('Nome do Produto: '))
    p = float(input('Preço: R$'))
    cont += 1
    total += p
    if p > 1000:
        totmil += 1
    if cont == 1 or p < menor:
        menor = p
        barato = n
    resp = ' '
    while resp not in 'SN':
        print('=='*10)
        resp = str(input('    Quer continuar? [S/N]')).strip().upper()[0]
        print('=='*10)
    if resp == 'N':
        break
print('FIM DO PROGRAMA...')
print(f'O total da compra foi de R${total:.2f} ')
print(f'Temos {totmil} produtos custando mais de R$1000.00 ')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f} ')