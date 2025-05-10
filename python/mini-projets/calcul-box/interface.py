""" Demander entrée utilisateur: """

def demander_nombre():
    while True:
        nbr = input("\n\tNombre : ").strip()
        try:
            if nbr.isdecimal():
                return int(nbr)
            else:
                return float(nbr)
        except:
            afficher_erreur(nbr)


def demander_operateur():
    while True:
        operateur = input("\n\tOpération (+ - * /): ").strip()
        if verifier_entrée(operateur, ["+", "-", "*", "/"]) is True and len(operateur) == 1 :
            return operateur
        else :
            afficher_erreur(operateur)



""" Retourner les erreurs """

def afficher_erreur(entrée) -> str:
    print(f"\t\nErreur,\"{entrée}\" est invalide")


def verifier_entrée(entrée_reçu, entrée_voulu: list) -> bool:
    return True if entrée_reçu in entrée_voulu else False


""" Afficher contenu de la box """

def afficher_total(box):
    print(f"\tTotal: {box.total:.2F}")


def afficher_calcul(box):
    print(f"Calcul: {box.to_string()}")
