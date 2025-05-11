from utils import check_str
from const import OPERATORS, RESET_BTN, ERROR_OPERATOR, ERROR_NUMBER

# === In ===

""" Get user input: """

def get_nbr():
        user_input = input("\n\tNumber:  ").strip()
        if check_str(user_input, digit=True):
            return int(user_input) if user_input.isdecimal() else round(float(user_input), 2)
        elif check_str(user_input, checkList=RESET_BTN):
            return user_input


def get_operator():
        user_input = input(f"\n\tOperator ? {OPERATORS}: ").strip()
        if check_str(user_input, checkList=OPERATORS+RESET_BTN):
            return user_input


# === Out ===

""" Calculator's display """

def display_total(box):
    print(f"\n\tTotal: \t{box.total:.2F}")


def display_calcul(box):
    print(f"\n\t{box.to_string()}")


""" Display errors """

def error(error_number:bool=None, error_operator:bool=None):
    if error_number:
        return ERROR_NUMBER

    elif error_operator:
        return ERROR_OPERATOR
