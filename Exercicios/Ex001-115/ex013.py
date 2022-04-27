s =  float(input('Qual o salário do funcionário? R$'))
a = (15 * s) / 100
ns = s + a
print('O aumento foi de:  R${:.2f} ao todo fica: R${:.2f}. '.format(a, ns))