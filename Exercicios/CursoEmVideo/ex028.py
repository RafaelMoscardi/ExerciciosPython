from random import randint
n = randint(0, 5)
print('---------------------------------------------------------------------------------')
print(' VOU PENSAR EM UM NUMERO DE 0 A 5. TENTE ADIVINHAR ')
print('---------------------------------------------------------------------------------')
escolhido = int(input('Qual número acha que eu escolhi? '))
print('Pensei no número... {} '.format(n))
if escolhido ==  n:
    print('PARABÉNS VOCÊ ADIVINHOU! ')
else:
    print('MAIS SORTE DA PRÓXIMA VEZ! ')


