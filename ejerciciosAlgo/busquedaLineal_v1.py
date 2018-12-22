# -*- coding: utf-8 -*-
valores = [23,4,67,32,13]

def busquedaLineal(lista, elemento):
    elemento = elemento
    posicionInicial = -1
    for i in lista:
        posicionInicial = posicionInicial + 1
        if i == elemento:
            break

    return lista, elemento, posicionInicial

busqueda = busquedaLineal(valores, 4)

print 'la lista es: '+ str(busqueda[0]) +'.  El elemento ' + str(busqueda[1]) + ' está en posición ' + str(busqueda[2])
