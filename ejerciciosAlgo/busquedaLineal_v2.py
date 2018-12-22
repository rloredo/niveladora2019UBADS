# -*- coding: utf-8 -*-
valores = [23,4,67,32,13, 22, 65, 22, 33, 90]

def busquedaLineal(lista, elemento):
    elemento = elemento
    posicionInicial = -1
    i = 0
    while i < len(lista):
        if lista[i] == elemento:
            posicionInicial = i
            #esto para salir del loop
            i = len(lista)
        else:
            posicionInicial = -1
        i = i + 1

    return elemento, posicionInicial



busqueda = busquedaLineal(valores, 5)

print 'la lista es: ' + str(valores)
if busqueda[1] != -1:
    print 'El elemento ' + str(busqueda[0]) + ' está en posición ' + str(busqueda[1])
else:
    print 'El elemento ' + str(busqueda[0]) + ' no está. Devuelve: ' + str(busqueda[1])
