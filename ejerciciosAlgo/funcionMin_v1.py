valores = [23,4,67,32, 444, 13, 2, -1]

def getMin(lista):
    inicio = 0
    fin = len(lista)
    if lista[inicio] < lista[inicio+1]:
        valorMin = lista[inicio]
    else:
        valorMin = lista[inicio+1]

    inicio = inicio + 2

    while inicio < fin:
        if lista[inicio] < valorMin:
            valorMin = lista[inicio]
        else:
            valorMin = valorMin
        inicio = inicio + 1

    return valorMin


print getMin(valores)
