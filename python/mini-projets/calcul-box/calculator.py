from interface import demander_nombre, demander_operateur

class Calculator:
    def __init__(self):
        self.operator = ""
        self.nbr = 0
        self.calcul = []
        self.total = 0


    def ajouter_nbr(self):
        self.nbr = demander_nombre()
        if str(self.nbr).isdecimal():
            self.calcul.append(self.nbr)
        else:
            self.calcul.append(format((self.nbr), ".2f"))
        self.calculer()


    def ajouter_operateur(self):
        self.operator = demander_operateur()
        self.calcul.append(self.operator)


    def reset_operateur(self):
        """ Vide la var operateur en fin de calcul """
        self.operator = ""


    def calculer(self):
        match self.operator:
            case "+":
                self.total = self.total + self.nbr

            case "-":
                self.total = self.total - self.nbr

            case "*":
                self.total = self.total * self.nbr

            case "/":
                self.total = self.total / self.nbr
            # If there no operator
            case _:
                self.total = self.nbr


    def to_string(self) -> str:
        """ change calcul list to string """
        string = str()
        for item in self.calcul:
            string = string+str(item)
        return string
