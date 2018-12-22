#Ordenamiento
valores = [59, 7, 388, 41, 7, 2, 280, 50, 123]

def ordenamiento(valores):
    temp = []
    i = 0
    largoInicial = len(valores)
    while i < largoInicial:
        j = i
        while j > 0 and valores[j - 1] > valores [j]:
            temp = valores[j - 1]
            valores[j - 1] = valores [j]
            valores[j] = temp
            j = j - 1
        i = i + 1
    return valores


print ordenamiento(valores)
