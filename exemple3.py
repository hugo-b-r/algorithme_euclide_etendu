from bibliotheque import *

a = 10110
b = 23454


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