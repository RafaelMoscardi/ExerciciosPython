da = float(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km rodados? '))
sd = da * 60
skm = km * 0.15
s = sd + skm
print('O total a pagar é de: R${:.2f}' .format(s))