while True:
        n = int(input('Digite um número para ver a sua Tabuada: '))
        if n < 0:
            break
        print('-=-' * 7)
        for c in range(1,11):
            print(f'{n} x {c} = {n*c}')
        print('-=-' * 7)
        print('Se quiser parar é so digitar um valor negátivo.')
print('UFA... Pensei que não iria parar!')