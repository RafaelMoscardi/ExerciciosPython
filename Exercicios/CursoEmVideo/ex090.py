aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 7:
    aluno['Situação'] = 'APROVADO!'
elif 5 <= aluno['media']  < 7:
    aluno['Situação'] = 'RECUPERAÇÃO!'
else:
    aluno['Situação'] = 'REPROVADO!'
print('-='*15)
for a, m in aluno.items():
    print(f'{a} é igual a {m}')