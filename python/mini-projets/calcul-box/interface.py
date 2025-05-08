""" Fonctions qui demande une entrée utilisateur: """

def demander_nombre():
    while True:
        nbr = input("\n\tNombre : ").strip()
        try:
            return float(nbr)
        except:
            afficher_erreur(nbr)
        
        
def demander_operateur():
    while True:
        operateur = input("\n\tOpération (+ - * /): ").strip()
        return operateur if verifier_entrée(operateur, ["+", "-", "*", "/"]) is True else afficher_erreur(operateur)



""" Fonctions qui retourne les erreurs """

def afficher_erreur(entrée) -> str:
    print(f"\tErreur,\"{entrée}\" est invalide")


def verifier_entrée(entrée_reçu, entrée_voulu: list) -> bool:
    return True if entrée_reçu in entrée_voulu else False