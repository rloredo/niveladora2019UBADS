
def potencia(n,m):
    if m == 0:
        return 1
    elif m == 1:
        return n
    else:
        return n * potencia(n, m - 1)


print potencia(8,2)
