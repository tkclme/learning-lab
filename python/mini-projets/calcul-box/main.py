from controller import loop_nbr, loop_operator
from calculator import Calculator



def main():
    calcul_box = Calculator()
    while True:
        loop_nbr(calcul_box)
        loop_operator(calcul_box)



if __name__ == "__main__":
    main()
