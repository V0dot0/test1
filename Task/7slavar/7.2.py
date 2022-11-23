# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye
key = []
slavar = {}
keySpecial = "None"
number = int(input(" Введите число: "))
while number != 0:
    inpud = input(" Введите слово и синоним: ")
    key = inpud[0]
    value = inpud[1]
    print(key, value)
    # key = input(" Введите слово: ")
    # value = input(" Введите его синоним: ")

    # slavar[value] = key
    if number - 1 == 0:
        keySpecial = input(" Введите финальный синоним: ")
        break
    number -= 1

# print (phone_book)
# print (keySpecial)
print(slavar.get(keySpecial))
