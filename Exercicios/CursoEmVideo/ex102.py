def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


n = int(input('Qual número deseja fatorar? '))
print(fatorial(n, show=True))
print(fatorial(n, show=False))



