lst = []

number = int(input(" Введите число строк: "))

while number != 0:
    key = input(" Введите список: ")
    words = key.split(' ')
    for word in words:
        lst.append(word)
    number -= 1
print(lst)

lst2 = {}
for i in lst:
    if i in lst2:
        lst2[i] += 1
    else:
        lst2[i] = 1

#print(lst2)
#maxNum = max(lst2.values())
maxNumKey = max(lst2, key=lst2.get)

print(maxNumKey)
