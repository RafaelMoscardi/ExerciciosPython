n = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
     'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
     'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
resp = ' '
while True:
    while True:
         num = int(input('Digite um número entre 0 e 20: '))
         if 0 <= num <= 20:
            break
         print('Tente novamente.', end=' ')
    print(f'Você digitou o número {n[num]}')
    resp = str(input('Deseja continuar?[S/N]: ')).upper().strip()
    if resp == 'N':
        break
    print('-=' * 16)