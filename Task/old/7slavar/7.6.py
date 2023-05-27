
lst = {}
number = int(input(" Введите число строк: "))

while number != 0:
    inpud = input(" ")
    key = inpud.split(" ", 1)
    key2 = str(key[:1])[2:-2]
    value = inpud.split(" ", 1)
    value2 = str(key[1:])[2:-2]

    lst[key2] = value2
    number -= 1

lstCheck = []
number = int(input(" Введите число : "))
while number != 0:
    inpud = input(" ")
    key = inpud.split(" ", 1)
    key2 = str(key[:1])[2:-2]

    for key, value in lst.items():
        if key2 in value:
            lstCheck.append(key)

    number -= 1

for i in lstCheck:
    print (i)

