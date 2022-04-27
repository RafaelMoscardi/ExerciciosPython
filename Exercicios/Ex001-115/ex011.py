h =  float(input('Qual a altura da parede ? '))
l = float(input('Qual a largura da parede? '))
a = h * l
tinta = a / 2
print('A área da parede é de: {:.2f}m² e é necessário {:.2f}L de tinta. '.format(a, tinta))