# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye

slavar = {}
sinonimSpecial = "None"
number = int(input(" Введите число: "))
while number != 0:
    inpud = input(" Введите слово и синоним: ").split(" ", 1)
    slovo = str(inpud[:1])[2:-2]
    sinonim = str(inpud[1:])[2:-2]
    slavar[sinonim] = slovo
    if number - 1 == 0:
        sinonimSpecial = input(" Введите финальный синоним: ")
        break
    number -= 1

print(slavar.get(sinonimSpecial))
