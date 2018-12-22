from Pila import *



def ejer1(l):
    print l
    p1 = Pila()
    p2 = []
    i = 0

    while i < len(l):
        p1.apilar(l[i])
        i = i + 1

    while not p1.vacia():
        p2.append(p1.tope())
        p1.desapilar()
    return p2

l1 = [1,2,3,4]
l2 = []
l3 = [3]

print 'Ejercicio 1'
print ejer1(l1)
print ejer1(l2)
print ejer1(l3)




def ejer2(s):
    print s,
    p1 = Pila()
    i = 0
    stringCompare = ''
    stringCompare2 = ''

    while i < len(s):
        if s[i] != '#':
            p1.apilar(s[i])
            i = i + 1
        else:
            stringCompare = s[i+1:len(s)]
            i = len(s)
    while not p1.vacia():
        stringCompare2 = stringCompare2 + p1.tope()
        p1.desapilar()

    return stringCompare == stringCompare2

s1 = 'abc#cba'
s2 = 'abba#abb'
s3 = '#'

print 'Ejercicio 2'
print ejer2(s1)
print ejer2(s2)
print ejer2(s3)
