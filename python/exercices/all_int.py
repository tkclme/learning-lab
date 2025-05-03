def all_int(exception:int, range=range(1, 21)):
    ints = []
    multiples = []
    for n in range:
        multiples.append(n) if (exception*n) == n*2 else ints.append(n)
    print(multiples)
    return ints
print(all_int(exception=3)) 
