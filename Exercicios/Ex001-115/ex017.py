co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = (ca ** 2 + co ** 2) ** (1/2)
print('A hipotenusa é: {:.2f}'.format(hi))

#OU      OU      OU      OU      OU      OU      OU      OU      OU      OU      OU      OU      OU      OU

import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = math.hypot(ca, co)
print('A hipotenusa é: {:.2f}'.format(hi))