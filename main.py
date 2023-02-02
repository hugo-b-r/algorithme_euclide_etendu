def ecrire_division_euclidienne(x, y):
    quotient = int(x/y)
    reste = x%y
    resultat = str(x) + " = " + str(y) + " x " + str(quotient) 
    resultat += " + " + str(reste)
    return resultat

def algorithme_euclide(a, b):
    if (a == b):
        return a
    elif (b > a):
        a += b
        b = a - b
        a = a - b
    return a