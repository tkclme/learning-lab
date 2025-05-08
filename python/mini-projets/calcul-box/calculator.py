from interface import demander_nombre, demander_operateur

class Calculator:
    def __init__(self):
        self.operator = ""
        self.nbr = 0
        self.calcul = list()
        self.total = 0
        
        
    def ajouter_nbr(self):
        self.nbr = demander_nombre()
        self.calculer()


    def ajouter_operateur(self):
        self.operator = demander_operateur()
    
    
    def reset_operateur(self):
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
                self.total = self.total + self.nbr
                
    
    def total(self):
        return self.total
        
    def afficher_calcul(self):
        return(self.calcul)