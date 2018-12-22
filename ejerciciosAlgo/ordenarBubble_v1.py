#Ordenamiento
valores = [59, 7, 388, 41, 7, 2, 280, 50, 123]

def ordenamiento(valores):
    temp = []
    i = 0
    while i < len(valores):
        j = 0
        while j < len(valores) - 1:
            if valores[j] > valores[j + 1]:

                temp = valores[j]
                valores[j] = valores [j + 1]
                valores[j + 1] = temp

            j = j + 1
        i = i + 1
    return valores

print ordenamiento(valores)
