lst = [int(s) for s in input().split()]
print(lst[2])
print(lst[-1])
print(lst[:5])
print(lst[0:-2])

lstNotChetniy = []; lstChetniy = []
for i in range(0, len(lst)):
    if i % 2 == 0:
        lstChetniy.append(lst[i])
    elif i % 2 == 1:
        lstNotChetniy.append(lst[i])
print (lstNotChetniy); print (lstChetniy)

print(lst[::-1])
print(lstChetniy[::-1])