from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade < 18:
    saldo = 18 - idade
    print('Seu alistamento será em {} anos.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos. '.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
elif idade == 18:
    print('Seu alistamento é NESSE ano! ')