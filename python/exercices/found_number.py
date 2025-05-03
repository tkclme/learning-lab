import random
import os

def clear():
    os.system("clear")

nbr = random.randrange(1, 99)
user_nbr = ""
indice = 100

clear()
while user_nbr != nbr:
    print("Devinez le nombre secret !\n")
    print(f"Indice : c'est moins de {indice}") if nbr <= indice else print(f"Indice : c'est plus de {indice}")
    user_nbr = input("\nEntrez votre reponse ici: ").strip()
    try:
        user_nbr = int(user_nbr)
        if user_nbr != nbr:
            clear()
            print("Eh non, essayez encore")
            indice = user_nbr
    except:
        clear()
        print("Il faut deviner un nombre\n")
clear()
print(f"Bravo, le nombre secret est bien {user_nbr}, vous avez gagné")
input()