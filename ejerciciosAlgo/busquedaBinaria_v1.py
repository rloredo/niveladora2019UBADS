# -*- coding: utf-8 -*-
valores = [0]
#Set high and low

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


print busquedaBinaria(valores, 2)
