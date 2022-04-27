from random import  randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('SUAS OPÇÕES: ')
print('[ 0 ] PEDRA ')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA ')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
print('KEN')
print('PO!')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
if computador == 0: #PEDRA
    if jogador == 0:
        print('EMPATE! ')
    elif  jogador == 1:
        print('JOGADOR VENCE! ')
    elif  jogador == 2:
        print('COMPUTADOR VENCE! ')
    else:
        print('JOGADA INVÁLIDA! ')
elif computador == 1: #PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE! ')
    elif jogador == 1:
        print('EMPATE! ')
    elif jogador == 2:
        print('JOGADOR VENCE! ')
    else:
        print('JOGADA INVÁLIDA! ')
elif computador == 2: #TESOURA
     if jogador == 0:
        print('JOGADOR VENCE! ')
     elif jogador == 1:
        print('COMPUTADOR VENCE! ')
     elif jogador == 2:
        print('EMPATE! ')
     else:
        print('JOGADA INVÁLIDA! ')