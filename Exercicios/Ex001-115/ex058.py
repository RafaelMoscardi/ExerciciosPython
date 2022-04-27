from random import randint
c = 1
print('Acabei de pensar em um número entre 0 e 10...')
print('Consegue adivinhar qual é?, Isso que vamos ver! ')
n = int(input('Qual é o seu palpite? '))
num = randint(0, 10)
while n != num:
    c += 1
    if n > num:
        print('MENOS... Tente mais uma vez.')
    else:
        print('MAIS... Tente mais uma vez.')
    n = int(input('Qual é o seu palpite? '))
    if n == num:
        print('Você adivinhou com {} tentativas, PARABÉNS! '.format(c))