lst = [int(s) for s in input().split()]
lst2 = [int(s) for s in input().split()]
lst3 = []
for i in range(0, len(lst)):
    if lst[i] == lst2[i]:
        lst3.append(lst[i])
final_number = len(lst3)
print(final_number)
