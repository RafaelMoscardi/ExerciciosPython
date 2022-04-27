sexo = str(input('Qual é o seu sexo? [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('INVÁLIDO!, informe seu sexo  [M/F]: ')).strip().upper()[0]
print('Sexo [{}] computado com sucesso! '.format(sexo))