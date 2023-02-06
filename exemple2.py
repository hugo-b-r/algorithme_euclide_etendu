from bibliotheque import *

a = 10110
b = 2353


print(
    ecrire_algorithme_euclide(
        algorithme_euclide(
            a,
            b
        )
    )
)

print(
    ecrire_algorithme_euclide_etendu(
        algorithme_etendu(
            algorithme_euclide(
                a,
                b
            )
        )
    )
)