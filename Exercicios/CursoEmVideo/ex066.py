n = s = c = 0
while True:
    n = int(input('Digite um número [999 para PARAR]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma entre {c} números é de {s}.')
print('FIM!')