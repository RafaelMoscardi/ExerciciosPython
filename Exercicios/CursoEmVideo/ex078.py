n = []
for c in range(0,5):
    n.append(int(input(f'Digite um valor para a posição {c}: ')))
print('=-=' * 15)
print(f'Você digitou os valores: {n}')
print(f'O maior valor dessa lista é: {max(n)} nas posições ', end=' ')
for i,v in enumerate(n):
    if v == max(n):
        print(f'{i}...', end=' ')
print()
print(f'O menor valor dessa lista é: {min(n)} nas posições ',end=' ')
for i,v in enumerate(n):
    if v == min(n):
        print(f'{i}...', end=' ')
print()