lista1 = [2,44,56,77,98,123]
lista2 = [3,22,56,65,68,77,80,98]

def enAmbasListas(l1, l2):
	rv = 0
	i = 0
	j = 0
    #Mientras i y j sean de longitud de su lista
	while i<len(l1) and j<len(l2):
        #Si es igual, pasar al siguiente elemento y sumar contador
		if l1[i]==l2[j]:
			rv = rv+1
			i = i+1
			j = j+1
        #Si elemento de lista 1 es menor al de lista 2, pasar al siguiente elemento de lista 1
		elif l1[i]<l2[j]:
			i = i+1
        #Si elemento de lista 1 es mayor a lista 2, pasar al siguiente elemento de lista 2
		else:
			j = j+1
	return rv


print enAmbasListas(lista1, lista2)
