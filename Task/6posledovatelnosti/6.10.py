# In the hole in the ground there lived a hobbit

lst = input()
lst1 = list(lst)
lastPart = lst[::-1][0: lst1.index("h") + 1]
lastPart = lastPart[::-1]
firstPart = lst[0: lst1.index("h")]
print(firstPart + lastPart)
