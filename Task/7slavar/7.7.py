#1 hi hi what is your name my name is bond james bond my name is damme van damme claude van damme jean claude van damme

lst = []

number = int(input(" Введите число строк: "))

while number != 0:
    key = input()
    words = key.split(' ')
    for word in words:
        lst.append(word)
    number -= 1

lst2 = {}
for i in lst:
    if i in lst2:
        lst2[i] += 1
    else:
        lst2[i] = 1

lst2 = dict(sorted(lst2.items()))
lst3 = sorted(lst2, key=lst2.get, reverse=True)
for sord in lst3:
    for key, value in lst2.items():
        if sord in key:
            print(sord, value)
