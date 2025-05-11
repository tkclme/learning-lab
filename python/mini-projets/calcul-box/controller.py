from const import TITLE, INFO, RESET_BTN

from interface import display_total, display_calcul, get_nbr, get_operator, error
import os

def display(box, issue):
    """
    Loop which display, title, info, calculation and total
    """
    os.system("clear")
    print(TITLE)
    print(INFO)
    if issue:
        print(issue)
    display_calcul(box)
    display_total(box)


def loop_nbr(box):
    """ Add a number in Calculator, print an error if there's not a valid input. """
    issue = ""
    while True:
        display(box, issue)
        nbr = get_nbr()
        if nbr:
            box.add_nbr(nbr)
            box.reset(RESET_BTN)
            box.calculer()
            break
        else: issue = error(error_number=True)


def loop_operator(box):
    """ Specifies an operator to the Calculator, print an error if there's not a valid input."""
    issue = None
    while True:
        display(box, issue)
        operator = get_operator()
        if operator:
            box.add_operator(operator)
            box.reset(RESET_BTN)
            break
        else:
            issue = error(error_operator=True)
