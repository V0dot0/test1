slavar = {}
number = int(input(" Введите число: "))
while number != 0:
    key = input(" Введите слово: ")
    value = input(" Введите его синоним: ")
    slavar[key] = value
    if number-1 == 0 :
        keySpecial = input(" Введите финальное слово: ")
        break
    number -= 1

#print (phone_book)
#print (keySpecial)
print (slavar.get(keySpecial))