import random
import os

nbr = random.seed(99)
user_nbr = ""
indice = 100

while user_nbr != nbr:
    print("Devinez le nombre secret !\n")
    print(f"Indice : c'est moins que {indice}") if nbr =< indice else print(f"Indice : c'est plus que {indice}")
    user_nbr = input("Entrez votre reponse ici: \n").strip()
    try:
        user_nbr = int(user_nbr)
        if user_nbr != nbr:
            print("Eh non, essayez encore!")
            indice = user_nbr
    except:
        print("Il faut deviner un nombre\n")
print(f"Bravo, le nombre secret est bien {user_nbr}, vous avez gagné")
input()