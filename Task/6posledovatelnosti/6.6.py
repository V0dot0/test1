lst1 = [int(s) for s in input().split()]
lst2 = [int(p) for p in input().split()]
lst3 = []
for i in range(0, len(lst1)):
    for j in range(0, len(lst2)):
        if lst1[i] == lst2[j]:
            lst3.append(lst2[j])
print (lst3)