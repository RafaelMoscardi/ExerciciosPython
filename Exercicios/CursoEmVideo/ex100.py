from random import randint
from time import sleep


def sort(lista):
    print('SORTEANDO 5 VALORES: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')

def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista}, temos: {soma}')


numeros = []
sort(numeros)
somapar(numeros)