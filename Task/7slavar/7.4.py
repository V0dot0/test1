# 2
# apple orange banana
# banana orange

lst = []

number = int(input(" Введите число строк: "))

while number != 0:
    key = input(" Введите список: ")
    words = key.split(' ')
    for word in words:
        lst.append(word)
    number -= 1
    lst.sort()

lst2 = {}
for i in lst:
    if i in lst2:
        lst2[i] += 1
    else:
        lst2[i] = 1

maxNumKey = max(lst2, key=lst2.get)

print(maxNumKey)
