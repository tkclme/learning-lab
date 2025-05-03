""" Convertisseur °C en °F & °C en °F """

def convert(temperature: int, into = "F"):
    return f"{temperature}°C -> {temperature*9/5 + 32}°F" if into == "F" else f"{temperature}°F -> {(temperature-32)*5/9}°C"

# Main loop
while True:
    # ajout de variable
    while True:
        temperature = input("Temperature à convertir: ").strip()
        try:
            temperature = int(temperature)
            break
        except:
            print(f"\nErreur, {temperature} n'est pas une entrée valide.")
            print("Veuillez entrer un nombre")
           
    # ajout de paramètres de conversion
    while True:
        print("\nType de conversion :\n")
        print("1 - °C to °F")
        print("2 - °F to °C\n")
        conversion = input("Entrez 1 ou 2, appuyez sur entrée pour valider: ").strip()
        if conversion in ["1", "2"]:
            print(int(convert(temperature))) if conversion == "1" else print(int(convert(temperature, "C")))
            break
        else : 
            print(f"\nErreur, {conversion} n'est pas une commande valide")
            print("Veuillez choisir entre 1 et 2\n")
            continue
        
    # quitter le programme ou continuer 
    while True:
        print("Voulez-vous effectuer une autre conversion?\n")
        choix = input("1 - Oui 2 - Non, appuyez sur entrée pour valider: \n").strip()
        if choix == "1":
            break
        elif choix == "2":
            quit()
        else :
            print(f"\nErreur, {choix} n'est pas une commande valide")
            print("Veuillez choisir entre 1 et 2\n")