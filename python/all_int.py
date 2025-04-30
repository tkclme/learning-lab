def all_int(exception: int, ensemble:range):
    ints = []
    multiples = []
    for n in ensemble:
        multiples.append(n*exception)
        ints.append(n) if n not in multiples else multiples.remove(n)
    return ints
        
print(all_int(3, range(1, 21)))