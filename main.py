def calculer_division_euclidienne(x, y):
    quotient = int(x/y)
    reste = x%y
    return (quotient, reste)
    



def ecrire_division_euclidienne(x, y, quotient, reste):
    texte = str(x) + " = " + str(y) + " x " + str(quotient) 
    texte += " + " + str(reste)
    return texte




# on peut creer une sorte de brique de construction pour les calculs
# mathématiques

class Brique:

    def __init__(self, termes = [], type = "rien"):
        self.termes = termes
        self.type = type



    
    def ecrire(self, brique):

        texte = ""
        elements_a_supprimer = []
        for partie in brique.termes:
            if (type(partie) == int):
                if (partie <= 0):
                    texte += "("
                    texte += str(partie)
                    texte += ")"
                else:
                    texte += str(partie)

            else:
                texte += "("
                texte += partie.ecrire(partie)
                texte += ")"
            
            if (brique.type == "somme"):
                    texte += " + "
            elif (brique.type == "produit"):
                    texte += " x "

        texte = texte[:-3]
        return texte



                

#difference1 = Brique([2, -3, -6], "somme")
#difference2 = Brique([4], "somme")
#difference3 = Brique([3], "somme")
#calculus = Brique([difference1, 4, 3], "produit")
#print(calculus.ecrire(calculus.developpe()))




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
#print(algorithme_euclide(198, 3100))



