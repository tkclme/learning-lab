# Écris une fonction smart_sum(*args, **kwargs) qui additionne tous les nombres en args, sauf ceux désignés comme ignore dans kwargs.
#Smart Sums

def smart_sum(*args, **kwargs):
    ignore = kwargs.get("ignore", [])
    return sum(i for i in args if i not in ignore)

print(smart_sum(1, 2, 3, 4, 5, ignore=(1, 2, 3)))
