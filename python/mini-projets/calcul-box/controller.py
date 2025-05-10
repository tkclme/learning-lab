from const import TITRE
from interface import afficher_total, afficher_calcul
import os

def afficher(box):
    """
    Boucle menu qui clean et affiche :
    - Titre
    - Info
    - Calcul en cours
    - Total
    """
    os.system("clear")
    print(TITRE)
    afficher_calcul(box)
    afficher_total(box)
