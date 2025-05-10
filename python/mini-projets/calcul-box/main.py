from controller import afficher
from calculator import Calculator


def main():
    calcul_box = Calculator()
    while True:
        afficher(calcul_box)
        calcul_box.ajouter_nbr()

        afficher(calcul_box)
        calcul_box.ajouter_operateur()



if __name__ == "__main__":
    main()
