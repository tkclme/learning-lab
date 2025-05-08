from controller import afficher
from calculator import Calculator


def main():
    calcul_box = Calculator()
    while True:
        #print(INFO)
        afficher(calcul_box)
        calcul_box.ajouter_nbr()
        
        afficher(calcul_box)
        calcul_box.ajouter_operateur()
        
        afficher(calcul_box)
        calcul_box.ajouter_nbr()
        calcul_box.reset_operateur()


if __name__ == "__main__":
    main()