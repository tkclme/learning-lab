class Calculator:
    def __init__(self):
        self.operator = ""
        self.nbr = 0
        self.calculation = []
        self.total = 0


    def add_nbr(self, nbr):
        self.nbr = nbr
        self.calculation.append(nbr)


    def add_operator(self, operator):
        self.operator = operator
        self.calculation.append(self.operator)


    def reset(self, reset_commands):
        """ Clean calculator """
        if self.nbr in reset_commands or self.operator in reset_commands:
            self.operator = ""
            self.nbr = 0
            self.calculation = []
            self.total = 0


    def calculate(self):
        match self.operator:
            case "+":
                self.total = self.total + self.nbr

            case "-":
                self.total = self.total - self.nbr

            case "*":
                self.total = self.total * self.nbr

            case "/":
                self.total = self.total / self.nbr
            # When starting without operator
            case _:
                self.total = self.nbr


    def to_string(self) -> str:
        """ change calculation list to string """
        string = str()
        for item in self.calculation:
            string = string+str(item)
        return string
