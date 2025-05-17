# Écris une fonction make_multiplier(n) qui retourne une fonction qui multiplie par n.
#make mutiplier
def make_multiplier(n):
    return lambda x: n * x

var = make_multiplier(4)
var(4) # 16

