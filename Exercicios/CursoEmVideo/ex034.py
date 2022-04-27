s = float(input('Qual é o salário do funcionário? R$'))
if s <= 1250:
    ns = s + (s * 15 / 100)
else:
        ns = s + (s *10 / 100)
print('Quem ganhava', s, 'Passa a ganhar R${:.2f} agora.'.format(ns))
