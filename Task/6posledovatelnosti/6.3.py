lst = [int(s) for s in input().split()]
lst2 = lst
i = 2
lst[0], lst[1] = lst[1], lst[0]
while i < len(lst):
    lst[i], lst[i+1] = lst[i+1], lst[i]
    i += 2
print (lst)