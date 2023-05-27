# Последний символ в строке в примере задачи не правильно выводится!!!!!!!


lst = input()
print(lst[2])
print(lst[-1])
print(lst[:5])
print(lst[0:-2])

lstNotChetniy = [];
lstChetniy = []
for i in range(0, len(lst)):
    if i % 2 == 0:
        lstChetniy.append(lst[i])
    elif i % 2 == 1:
        lstNotChetniy.append(lst[i])

print(str(lstNotChetniy).replace("[", "").replace("]", "").replace(",", "").replace("'", "").replace(" ", ""))
print(str(lstChetniy).replace("[", "").replace("]", "").replace(",", "").replace("'", "").replace(" ", ""))
print(lst[::-1])
print(str(lstChetniy[::-1]).replace("[", "").replace("]", "").replace(",", "").replace("'", "").replace(" ", ""))
