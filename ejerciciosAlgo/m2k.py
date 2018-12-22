# -*- coding: utf-8 -*-
#Conversor millas a km
print "Bienvenido al conversor millas a km. Ingrese un número a convertir o escriba chau para salir"

#Pide input usuario
inputUsuario = raw_input()

#Ciclo indefinido hasta que se cierre
while inputUsuario != 'chau':
   # Si puede convertir a float pasa al ELSE
    try:
        float(inputUsuario)
    #Si no se puede convertir a float no escribió un número
    except ValueError:
        #Si escribió Chau con mayúscula, sale igual pero te hace notar
        if inputUsuario == 'Chau':
            print 'Dije escribir chau, no Chau. Pero igual te entendí. Nos vemo!'
            exit()
        #Si escribió cualquier cosa, avisa y da la opción para volver a intentar
        else:
            print 'Ingresó cualquier cosa...'
            print 'Ingrese un número a convertir o chau para salir...'
            inputUsuario = raw_input()
    #Se ejecuta solo si puede convertir a float.
    #Evitamos poner todo en el try por si el error no es en otro lado diferente del float
    else:
        km = str(round(float(inputUsuario)*1.60934, 2))
        #Imprime la conversión y deja abierto para hacer otra consulta
        print inputUsuario + ' millas son ' + km + ' kilómetros.'
        print 'Ingrese otro número a convertir o chau para salir...'
        inputUsuario = raw_input()


#si termina el ciclo (porque el input es chau) sale
print 'Chau, nos vemo!'
exit()
