import math

# Abrakadabra

lst = input()
lst1 = list(lst)
k = float(len(lst1)) / 2
max = math.ceil(k)
lst2 = lst1[max: len(lst1)] + lst1[0: max]
print(str(lst2).replace("[", "").replace("]", "").replace(",", "").replace("'", "").replace(" ", ""))
