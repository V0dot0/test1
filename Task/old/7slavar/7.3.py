slavar = {}

number = int(input(" Введите число: "))
while number != 0:
    inpud = input(" Введите слово и синоним: ").split(" ", 1)
    key = str(inpud[:1])[2:-2]
    value = int(str(inpud[1:])[2:-2])

    # key = input(" Введите президента: ")
    # value = int(input(" Введите его голоса : "))

    if key not in slavar:
        slavar[key] = value
    else:
        slavar[key] += value
    number -= 1

print(str(slavar).replace("{", "").replace("}", "").replace(",", "\n").replace("'", "").replace(":", ""))
