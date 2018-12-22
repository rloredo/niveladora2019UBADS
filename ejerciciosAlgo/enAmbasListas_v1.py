lista1 = [2,44,56,77,98,123]
lista2 = [3,22,56,65,68,77,80,98]


def busquedaBinaria(lista, elemento):
    inicio = 0
    final = len(lista) - 1
    while(inicio <= final):
        medio = (inicio + final) / 2
        if lista[medio] < elemento:
            inicio = medio + 1
        elif lista[medio] > elemento:
            final = medio - 1
        else:
            return medio

    return -1

def enAmbasListas(listaOrigen, listaMeta):
    i = 0
    cantidad = 0
    repetidos = []
    while i < len(listaOrigen):
        esta = busquedaBinaria(listaMeta, listaOrigen[i])
        if esta != -1:
            repetidos.append(listaOrigen[i])
            cantidad = cantidad + 1
        i = i + 1
    return cantidad, repetidos

busqueda = enAmbasListas(lista2, lista1)

print 'Encontrados ' + str(busqueda[0]) + ' repetidos. Son: ' + str(busqueda[1])
