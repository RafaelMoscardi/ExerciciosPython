maior = 0
menor = float('inf')
for c in range(1,6):
    p = float(input('Peso {}ª pessoa: '.format(c)))
    if p>maior:
        maior = p
    if p<menor:
        menor = p
print('Dentre esses, o maior peso foi {}Kg e o menor foi {}Kg '.format(maior, menor))