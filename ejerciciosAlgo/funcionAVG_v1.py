valores = [23,4,67,32, 13]

def computeMean(lista):
    inicio = 1
    fin = len(lista)
    suma = lista[0]

    while inicio < fin:
        suma = suma + lista[inicio]
        inicio = inicio + 1

    promedio = round(float(suma)/fin, 2)

    return promedio

print computeMean(valores)
