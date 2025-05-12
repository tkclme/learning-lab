def PGCD(nbr1:int, nbr2:int, methode="list" or "eucl") -> int:
    """
    Return PGCD of two number\n
    You can use two algorithmes, list methode or Euclidean division by enter "list" or "eucl" in "methode" parameter, default is "list".\n
    Be careful when using big number.
    
    """
    
    if methode=="list":
        
        diviseurs_nbr1 = []
        diviseurs_nbr2 = []
        diviseurs_commun = []
        
        for n in range(1, nbr1+1):
            if (nbr1/n) == int(nbr1/n): diviseurs_nbr1.append(n)
            
        for n in range(1, nbr2+1):
            if (nbr2/n) == int(nbr2/n): diviseurs_nbr2.append(n)

        more_lengh_lst = diviseurs_nbr1 if len(diviseurs_nbr1) >= len(diviseurs_nbr2) else diviseurs_nbr2
           
        for n in more_lengh_lst:
            if n in diviseurs_nbr1 and n in diviseurs_nbr2:
                diviseurs_commun.append(n)

        return diviseurs_commun[len(diviseurs_commun)-1]

    elif methode == "eucl":
        if nbr1 >= nbr2:
            dividende = nbr1
            diviseur = nbr2
        else :
            dividende = nbr2
            diviseur = nbr1
        
        reste = int
        quotient = int
        while reste != 0:
            quotient = int(dividende/diviseur)
            reste = dividende-(quotient*diviseur)
            dividende = diviseur
            diviseur = reste
        return dividende