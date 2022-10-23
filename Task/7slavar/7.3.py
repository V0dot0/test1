slavar = {}

number = int(input(" Введите число: "))
while number != 0:
    key = input(" Введите президента: ")
    value = int(input(" Введите его голоса : "))
    if key not in slavar :
        slavar[key] = value
    else:
        slavar[key] += value
    number -= 1

print (slavar)