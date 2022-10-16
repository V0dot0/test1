lst = [int(s) for s in input().split()]
for i in range(0, len(lst)):
    if lst[i] == max(lst) :
        mai = i
    if lst[i] == min(lst) :
        mini = i
lst[mini], lst[mai] = lst[mai], lst[mini]
print(lst)