valores = [23,4,67,32, -300,444, 13, 2, -1]

def getMin(lista):
    inicio = 1
    fin = len(lista)
    valorMin = lista[0]
    while inicio < fin:
        if valorMin > lista[inicio]:
           valorMin = lista[inicio]
        else:
            valorMin = valorMin
        inicio = inicio + 1
    return valorMin

print getMin(valores)
