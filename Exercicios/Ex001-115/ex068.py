from random import randint
print('-=-' * 11)
print('  VAMOS JOGAR PAR OU ÍMPAR  ')
print('-=-' * 11)
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
          tipo = str(input('PAR OU IMPAR? [P/I]')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU! ')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU! ')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(F'GAME OVER! Você venceu {v} vezes. ')