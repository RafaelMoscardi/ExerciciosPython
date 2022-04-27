print('===== LOJAS MOSCARDI =====')
p = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque ')
print('[ 2 ] à vista cartão ')
print('[ 3 ] 2x no cartão ')
print('[ 4 ] 3x ou mais no cartão ')
esc = int(input('Qual é a opção? '))
if esc == 1:
    np = p - (p * 10/100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p, np))
elif esc == 2:
    np = p - (p * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p, np))
elif esc == 3:
    par = int(input('Quantas parcelas? '))
    parc = p / par
    print('Sua compra será parcelada em {}x de R${:.2f} SEM JUROS.'.format(par, parc))
    print('Sua compra vai custar R${:.2f} no final.'.format(p))
elif esc == 4:
    par = int(input('Quantas parcelas? '))
    np = p + (p * 20 / 100)
    parc = np / par
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(par, parc))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p, np))
else:
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE! ')
