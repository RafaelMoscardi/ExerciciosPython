num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] converter para BINÁRIO ')
print('[ 2 ] converter para OCTAL ')
print('[ 3 ] converter para HEXADECIMAL ')
esc = int(input('Sua opção: '))
if esc == 1:
    print('Em BINÁRIO é {}'.format(bin(num)[2:]))
elif esc == 2:
    print('Em OCTAL é {}'.format(oct(num)[2:]))
elif esc == 3:
    print('Em HEXADECIMAL é {}'.format(hex(num)[2:]))
else:
   print('OPÇÃO INVALIDA! ')