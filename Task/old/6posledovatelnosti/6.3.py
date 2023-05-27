lst = [int(s) for s in input().split()]
i = 1
while i < len(lst):
    lst[i - 1], lst[i] = lst[i], lst[i - 1]
    i += 2
print(str(lst).replace("[", "").replace("]", "").replace(",", ""))
