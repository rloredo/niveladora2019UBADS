#Ordenamiento
valores = [59, 7, 388, 41, 2, 280, 50, 123]

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

def ordenamiento(valores):
    temp = []
    i = 0
    largoInicial = len(valores)
    while i < largoInicial:
        minimo = getMin(valores)
        temp.append(minimo)
        valores.remove(minimo)
        i = i + 1
    return temp


print ordenamiento(valores)
