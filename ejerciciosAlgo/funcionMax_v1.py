valores = [23,4,67,32, -300,444, 13, 2, -1, 123123123]

def getMax(lista):
    inicio = 1
    fin = len(lista)
    valorMax = lista[0]
    while inicio < fin:
        if valorMax < lista[inicio]:
           valorMax = lista[inicio]
        else:
            valorMax = valorMax
        inicio = inicio + 1
    return valorMax

print getMax(valores)
