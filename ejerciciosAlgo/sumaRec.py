lista1 = [1,1,1,1,2,3]

def suma(l):
    if len(l) > 1:
        return  l[0] + suma(l[1:len(l)])
    else:
        return l[0]

print suma(lista1)
