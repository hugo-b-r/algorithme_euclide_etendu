import math




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



    # on developper mais seulement un produit de deux termes à la fois
    # donc on crée une nouvelle brique qui contiendra seulement deux termes
    def developpe(self):
        if (self.type == "produit"):
            #ATTENTION, NE DEVELEOPPE QUE LES DEUX PREMIERS TERMES
            resultat = Brique([], "somme")
            
            #on developpe le produit actif
            for i in self.termes[0].termes:
                for j in self.termes[1].termes:
                    produit_intermediaire = Brique([j, i], "produit")
                    resultat.termes.append(produit_intermediaire)
            return resultat

        else:
            print("erreur: developpe: pas un produit")
            exit()
    


    def ecrire(self):

        texte = ""
        elements_a_supprimer = []
        for partie in self.termes:
            if (type(partie) == int):
                if (partie <= 0):
                    texte += "("
                    texte += str(partie)
                    texte += ")"
                else:
                    texte += str(partie)

            else:
                texte += "("
                texte += partie.ecrire()
                texte += ")"
            
            if (self.type == "somme"):
                    texte += " + "
            elif (self.type == "produit"):
                    texte += " x "

        texte = texte[:-3]
        return texte




#une fonction qui renvoie une liste a deux dimensions, cahque "ligne", sera
# de longueur 4, le dividende, le quotient, le diviseur et le reste
def algorithme_euclide(a, b):
    if (a == b):
        return a
    elif (b > a):
        a += b
        b = a - b
        a = a - b
    
    quotient = 1
    reste = 1
    algorithme = []
    while (reste != 0):
        div_euclidienne = calculer_division_euclidienne(a, b)
        quotient = div_euclidienne[0]
        reste = div_euclidienne[1]
        algorithme.append([a, b, quotient, reste])
        a = b
        b = reste
    return algorithme




def ecrire_algorithme_euclide(algorithme_euclide):
    texte = ""
    for ligne in algorithme_euclide:
        texte += str(ligne[0])
        texte += " = "
        texte += str(ligne[1])
        texte += " x "
        texte += str(ligne[2])
        texte += " + " 
        texte += str(ligne[3])
        texte += "\n"
    return texte




def pgcd(a, b):
    while a != b:
        d = math.abs(b-a)
        b = a
        a = d
    return d





# directive: bien penser à mettre d'abord le diviseur, puis le quotient
# (dans toute structure possible)
def algorithme_etendu(algorithme_euclide):
    texte = ""
    i = 0
    # on "positionne" i à l'étape où il y a 1 comme reste
    while (algorithme_euclide[i][3]  != 1):
        i += 1
    expressions = []
    #on met la premiere expression dans la boite
    expression = Brique ([
        algorithme_euclide[i][0],
        -Brique ([
            algorithme_euclide[i][1],
            algorithme_euclide[i][2]
            ],
            "produit"
        )],
        "somme"
    )
    expressions.append(expression)


    while i > 0:
        #etape 1: on remplace par dividende - diviseur x quotient a i-1
        expression.termes[1].termes[0] = Brique ([
            algorithme_euclide[i-1][0],
            -Brique ([
                algorithme_euclide[i-1][1],
                algorithme_euclide[i-1][2]
                ],
                "produit"
            )],
            "somme"
        )
        expressions.append(expression)

        #etape 2: on developpe
        developpement = expression.termes[1].developpe()
        #on transforme le deuxieme produit du develppement en un simple
        developpement[1] = Brique ([
            developpement[1].termes[0].termes[0],
            developpement[1].termes[0].termes[1] * developpement[1].termes[1].termes[0]
            ],
            "produit"
        )

        expression.pop(1)
        for sous_expression in developpement:
            expression.append(sous_expression) 
        expressions.append(expression)

        #etape 3: on rassemble/simplifie
        for i in range (len(developpement)):
            try:
                if (expression[0].termes[0] == expression[i].termes[0]):
                    expression[0].termes[1] += expression[i].termes[1]
                    expression.pop(i)   # on remet l'expression en etat pour que 
                                        # le prochain changé soit en deuxieme rang
            finally:
                pass
            expressions.append(expression)

        i -= 1
    return expressions


