lista1 = [7,2,3]

def maxRec(l):
    if len(l) > 2:
        if l[0] > maxRec(l[1:len(l)]):
            return l[0]
        else:
            return maxRec(l[1:len(l)])
    else:
        if l[0] > l[1]:
            return l[0]
        else:
            return l[1]

print maxRec(lista1)
