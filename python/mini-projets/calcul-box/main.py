from interface import TITRE
from calculator import Calculator


def main():
    calcul_box = Calculator()
    while True:
        print(TITRE)
        #print(INFO)
        calcul_box.afficher_total()
        calcul_box.ajouter_nbr()
        calcul_box.afficher_total()
        calcul_box.ajouter_operateur()
        calcul_box.calculer()



if __name__ == "__main__":
    main()