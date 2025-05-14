# Écris une fonction smart_sum(*args, **kwargs) qui additionne tous les nombres en args, sauf ceux désignés comme ignore dans kwargs.

def smart_sum(*args, **kwargs):
    result = []
    for i in args:
        if i not in kwargs["ignore"]:
            result.append(i)
    return sum(result)

print(smart_sum(1, 2, 3, 4, 5, ignore=(1, 2, 3)))
