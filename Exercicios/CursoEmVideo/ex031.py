km = float(input('Digite a distância da viagem: '))
print('Você está prestes a embarcar em uma viagem de {}Km '.format(km))
if km <= 200:
    v = km * 0.50
else:
    v = km * 0.45
print('O preço da passagem será: R$ {:.2f} '.format(v))