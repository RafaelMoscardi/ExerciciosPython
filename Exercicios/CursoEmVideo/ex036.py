v = float(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
a = int(input('Quantos anos de financiamento? '))
prest = v / (a * 12)
min = s *30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(v, a, prest))
if prest <= min:
    print('EMPRÉSTIMO ACEITO! ')
else:
    print('EMPRÉSTIMO NEGADO! ')