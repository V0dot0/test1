lst = {}
number = int(input(" Введите число строк: "))

while number != 0:
    inpud = input(" ")
    key = inpud.split(" ", 1)
    key2 = str(key[:1])[2:-2]

    value2 = str(key[1:])
    value2 = str(value2.split())
    value3 = list(value2)

    lst[key2] = value3
    number -= 1

lstCheck = []
number = int(input(" Введите число строк: "))
while number != 0:
    inpud = input(" ")
    key = inpud.split(" ", 1)
    key2 = str(key[:1])[2:-2]
    value = inpud.split(" ", 1)
    value2 = str(key[1:])[2:-2]

    match key2:
        case 'read':
            if 'R' in lst[value2]:
                lstCheck.append("ok")
            else:
                lstCheck.append("Denied")
        case 'write':
            if 'W' in lst[value2]:
                lstCheck.append("ok")
            else:
                lstCheck.append("Denied")
        case 'execute':
            if 'E' in lst[value2]:
                lstCheck.append("ok")
            else:
                lstCheck.append("Denied")

    number -= 1
for i in lstCheck:
    print (i)
# it just works