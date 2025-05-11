class Calculator:
    def __init__(self):
        self.operator = ""
        self.nbr = 0
        self.calcul = []
        self.total = 0


    def add_nbr(self, nbr):
        self.nbr = nbr
        self.calcul.append(nbr)


    def add_operator(self, operator):
        self.operator = operator
        self.calcul.append(self.operator)


    def reset(self, reset_commands):
        """ Clean calculator """
        if self.nbr in reset_commands or self.operator in reset_commands:
            self.operator = ""
            self.nbr = 0
            self.calcul = []
            self.total = 0



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
