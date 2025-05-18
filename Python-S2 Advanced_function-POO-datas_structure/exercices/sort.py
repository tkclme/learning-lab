# Ecris une fonction qui trie une liste

def mySortFunction(iteration) -> list:
    liste = iteration.copy()
    sorted_liste = []
    index = len(liste)
    for i in range(index):
        for j in range(index):
            if liste[i] < liste[j]:
                continue
            else: 
                break
            sorted_liste.append(liste[i])
    return sorted_liste
a = [9, 5, 7, 3, 1]
print(mySortFunction(a))