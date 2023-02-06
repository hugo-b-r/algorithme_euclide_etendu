from bibliotheque import *


a = 21
b = 1234567890

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