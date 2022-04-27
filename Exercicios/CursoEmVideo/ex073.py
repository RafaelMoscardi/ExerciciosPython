times = ('America-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Avaí',
                'Botafogo', 'Ceará SC', 'Corinthians', 'Coritiba', 'Cuiabá', 'Flamengo',
                'Fluminense', 'Fortaleza', 'Goiás', 'Internacional', 'Juventude',
                'Palmeiras', 'Bragantino', 'Santos', 'São Paulo')
print(f'Lista de times do Brasileirão 2022: {times}')
print('-=-'*14)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=-'*14)
print(f'Os 4 últimos são: {times[16:]}')
print('-=-'*14)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=-'*14)
print('O Coritiba está na', times.index('Coritiba')+1,'ª da tabela')