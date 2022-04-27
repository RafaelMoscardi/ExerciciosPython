# VALORES
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opc = 0
while opc != 5:
    print('[ 1 ] SOMAR ')
    print('[ 2 ] MULTIPLICAR ')
    print('[ 3 ] MAIOR ')
    print('[ 4 ] NOVOS NÚMEROS ')
    print('[ 5 ] SAIR DO PROGRAMA ')
    opc = int(input('Escolha um opção: '))
# SOMA
    if opc == 1:
        soma = v1 + v2
        print('Resultado de {} + {} é {} '.format(v1, v2, soma))
# MULTIPLICAÇÃO
    elif opc == 2:
        mult = v1 * v2
        print('Resultado de {} x {} é {} '.format(v1, v2, mult))
 # MAIOR
    elif opc == 3:
        if v1 > v2:
            print('Entre {} e {} o MAIOR é {} '.format(v1, v2, v1))
# IGUAIS
        elif v1 == v2:
            print('{} e {} são IGUAIS'.format(v1, v2))
 # MAIOR
        else:
            print('Entre {} e {} o MAIOR é {} '.format(v1, v2, v2))
# OUTROS VALORES
    elif opc == 4:
        print('Informe os números novamente: ')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
# FINALIZAR
    elif opc == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente! ')
    print('=========================')
print('Fim do programa! Volte sempre!')