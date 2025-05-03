from interface import demander_nombre, demander_operateur

class Calculator:
    def __init__(self):
        self.operator = ""
        self.nbr = 0
        self.total = 0
        
        
    def ajouter_nbr(self):
        self.nbr = demander_nombre()

    def ajouter_operateur(self):
        self.operator = demander_operateur()
    
    
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
    
    
    def afficher_total(self):
        print(f"\n\tTotal: {self.total:.2F}")