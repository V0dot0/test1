lst = [int(s) for s in input().split()]
for i in range(0, len(lst)):
    if i == lst.index(lst[i]):
        print("НЕТ")
    else:
        print("ДА")