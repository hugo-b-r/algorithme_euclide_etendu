def calculer_division_euclidienne(x, y):
    quotient = int(x/y)
    reste = x%y
    return (quotient, reste)
    

def ecrire_division_euclidienne(x, y, quotient, reste):
    texte = str(x) + " = " + str(y) + " x " + str(quotient) 
    texte += " + " + str(reste)
    return texte





def algorithme_euclide(a, b):
    if (a == b):
        return a
    elif (b > a):
        a += b
        b = a - b
        a = a - b
    
    #initialisons une liste pour y stocker les quotients
    texte = ""
    quotient = 1
    reste = 1
    while (reste != 0):
        div_euclidienne = calculer_division_euclidienne(a, b)
        quotient = div_euclidienne[0]
        reste = div_euclidienne[1]
        texte += ecrire_division_euclidienne(a, b, quotient, reste)
        texte += "\n"
        a = b
        b = reste
    return texte
print(algorithme_euclide(19, 11))