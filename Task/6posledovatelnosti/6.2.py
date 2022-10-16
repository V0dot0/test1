lst = [int(s) for s in input().split()]
lst2=[]
for i in range(0, len(lst)):
    if lst[i]>lst[i-1] :
        lst2.append(lst[i])
print (lst2)