def ecrire_division_euclidienne(x, y):
    quotient = int(x/y)
    reste = x%y
    resultat = str(x) + " = " + str(y) + " x " + str(quotient) 
    resultat += " + " + str(reste)
    return resultat
