p =  float(input('Qual o preço do produto? '))
d = (5 * p) / 100
np = p + d
print('O preço do produto era de:  R${:.2f} e com desconto: R${:.2f}. '.format(p, np))