valores = [2, 3, 3, 5, 5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def ordenarLineal(lista):
    i = 0
    j = 0
    while i < 10 and j <= len(lista):
        if lista[j] != i:
            j = j + 1
        else:
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp
            i = i + 1
    return lista


print ordenarLineal(valores)
