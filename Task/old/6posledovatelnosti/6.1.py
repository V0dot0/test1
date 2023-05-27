lst = [int(s) for s in input().split()]
lst2 = [int(s) for s in lst if s % 2 == 1]
print(str(lst2).replace("[", "").replace("]", "").replace(",", ""))
