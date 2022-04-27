from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os números sorteados foram: \n{n}')
print('=-' * 15)
print(f'O maior valor sorteado foi: {max(n)}')
print('=-' * 15)
print(f'O menor valor sorteado foi: {min(n)}')
print('=-' * 15)