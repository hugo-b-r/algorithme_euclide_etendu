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
            if ((type(self.termes[0]) == int) and (type(self.termes[1]) != int)):
                for i in self.termes[1].termes:
                    produit_intermediaire = Brique([self.termes[0], i], "produit")
                    resultat.termes.append(produit_intermediaire)

            elif ((type(self.termes[0]) != int) and (type(self.termes[1]) == int)):
                for i in self.termes[0].termes:
                    produit_intermediaire = Brique([i, self.termes[1]], "produit")
                    resultat.termes.append(produit_intermediaire)

            if ((type(self.termes[0]) != int) and (type(self.termes[1]) != int)):
                #on developpe le produit actif
                for i in self.termes[0].termes:
                    for j in self.termes[1].termes:
                        produit_intermediaire = Brique([j, i], "produit")
                        resultat.termes.append(produit_intermediaire)

            if ((type(self.termes[0]) != int) and (type(self.termes[1]) != int)):
                resultat.append(Brique([self.termes[0], self.termes[1]], "produit"))
            
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
        d = abs(b-a)
        b = a
        a = d
    return d





# directive: bien penser à mettre d'abord le diviseur, puis le quotient
# (dans toute structure possible)
# bien utilise des nombres premiers entre eux !!!
def algorithme_etendu(algorithme_euclide):
    
    if (pgcd(algorithme_euclide[0][0], algorithme_euclide[0][1]) != 1):
        return "non premiers entre eux"


    texte = ""
    i = 0
    # on "positionne" i à l'étape où il y a 1 comme reste
    while (algorithme_euclide[i][3]  != 1):
        i += 1
    expressions = []
    #on met la premiere expression dans la boite
    expression = Brique ([
        algorithme_euclide[i][0],
        Brique ([
            algorithme_euclide[i][1],
            -algorithme_euclide[i][2]
            ],
            "produit"
        )],
        "somme"
    )
    print(expression.ecrire())
    expressions.append(expression)


    while i > 0:
        #etape 1: on remplace par dividende - diviseur x quotient a i-1
        expression.termes[1].termes[0] = Brique([
            algorithme_euclide[i-1][0],
            Brique ([
                algorithme_euclide[i-1][1],
                -algorithme_euclide[i-1][2]
                ],
                "produit"
            )],
            "somme"
        )
        print(expression.ecrire())
        expressions.append(expression)

        #etape 2: on developpe
        developpement = expression.termes[1].developpe()
        #on transforme le deuxieme produit du develppement en un simple
        terme1 = developpement.termes[1].termes[0].termes[0]
        terme2 = developpement.termes[1].termes[0].termes[1]
        terme3 = developpement.termes[1].termes[1]
        term_prod = terme2 * terme3
        developpement.termes[1] = Brique([
            terme1,
            terme2 * terme3
            ],
            "produit"
        )

        expression.termes.pop(1)
        for sous_expression in developpement.termes:
            expression.termes.append(sous_expression)
        print(expression.ecrire())
        expressions.append(expression)

        #etape 3: on rassemble/simplifie
        for i in range (len(developpement.termes)-1):
            if (type(expression.termes[0]) != int):
                if (expression.termes[0].termes[0] == expression.termes[i].termes[0]):
                    expression.termes[0].termes[1] += expression.termes[i].termes[1]
                    expression.pop(i)   # on remet l'expression en etat pour que 
                                        # le prochain changé soit en deuxieme rang
            if (type(expression.termes[0]) == int):
                if (expression.termes[0] == expression.termes[i+1].termes[0]):
                    expression.termes[0] = Brique([
                        expression.termes[0],
                        1 + expression.termes[i][1]
                        ],
                        "produit"
                    )
                    expression.pop(i)

            print(expression.ecrire())
            expressions.append(expression)

        i -= 1
    return expressions




def ecrire_algorithme_euclide_etendu(algo_etendu):
    texte = ""
    for i in range (len(algo_etendu)):
        texte += f"1 = {algo_etendu[i].ecrire()}\n"
    return texte

print(
    ecrire_algorithme_euclide(
        algorithme_euclide(124, 57)
    )
)
ecrire_algorithme_euclide_etendu(
    algorithme_etendu(
        algorithme_euclide(
            124,
            57
        )
    )
)

